import requests
import matplotlib.pyplot as plt
import concurrent.futures
import yaml
from datetime import date
from utils import MatchData
from PIL import Image
import base64
import io

yaml_file = yaml.load(open("keys.yaml"), Loader=yaml.FullLoader)

time_constant = 9999999999999

auth = yaml_file['auth']

headers={
        'X-TBA-Auth-Key': auth
        }

def getRookieYear(team1, team2):
    link = "https://www.thebluealliance.com/api/v3/team/frc"
    data1=requests.get(url=link+str(team1), headers=headers).json()
    data2=requests.get(url=link+str(team2), headers=headers).json()
    return max(data1['rookie_year'], data2['rookie_year'])

def getRecord(firstTeam, secondTeam):
    results={
                firstTeam:0, 
                secondTeam:0, 
                "tie":0
            }
    threads=[]
    matches={}
    current_year = date.today().year
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for year in range(getRookieYear(firstTeam, secondTeam), current_year+1):
            thread = executor.submit(getDataForYear, year, firstTeam, secondTeam)
            threads.append(thread)
    for thread in threads:
        result, newMatches, year = thread.result()
        results[firstTeam]=results[firstTeam]+result[firstTeam]
        results[secondTeam]=results[secondTeam]+result[secondTeam]
        results['tie']=results['tie']+result['tie']
        matches[year]=newMatches
    total=results[firstTeam]+results[secondTeam]+results['tie']
    if total==0:
        im = Image.open("static/no_data.png")
        img = io.BytesIO()
        im.save(img, "png")
        return [], base64.b64encode(img.getvalue()).decode('utf-8')
    labels = []
    sizes = []
    if results[firstTeam]!=0:
        labels.append(firstTeam)
        sizes.append(100*results[firstTeam]/total)
    if results[secondTeam]!=0:
        labels.append(secondTeam)
        sizes.append(100*results[secondTeam]/total)
    if results['tie']!=0:
        labels.append("Tie")
        sizes.append(100*results['tie']/total)
    _, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',startangle=90)
    ax1.axis('equal') 
    plt.legend()
    plt.title("H2H Record")
    plt.figtext(.5, .05, str(firstTeam)+" "+str(results[firstTeam])+":"+str(results[secondTeam])+" "+str(secondTeam), ha='center')
    dict(sorted(matches.items()))
    info=[]
    for year in matches:
        for match in matches[year]:
            info.append(match)
    img = io.BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode('utf8')
    return info, graph_url
    

def getDataForYear(year, firstTeam, secondTeam):
    results={
                firstTeam:0, 
                secondTeam:0, 
                'tie':0
            }
    matches=[]
    try:
        link = "https://www.thebluealliance.com/api/v3/team/frc"+str(firstTeam)+"/matches/"+str(year)
        data=requests.get(url=link, headers=headers).json()
    except Exception:
        print("Could not pull data")
    try:
        for result in data:
            if matchHappened(result) and (oppositeAlliances(result, firstTeam, secondTeam,'red') or oppositeAlliances(result, firstTeam, secondTeam,'blue')):
                if int(result['alliances']['red']['score'])<int(result['alliances']['blue']['score']):
                    winner = 'blue'
                if int(result['alliances']['red']['score'])>int(result['alliances']['blue']['score']):
                    winner='red'
                elif int(result['alliances']['red']['score'])==int(result['alliances']['blue']['score']):
                    winner='none'
                try:
                    time = int(result['actual_time'])
                except Exception:
                    time = time_constant
                if "frc"+str(firstTeam) in result['alliances']['blue']['team_keys']:
                    mainTeamAlliance='blue'
                    matches.append(
                                    MatchData(
                                        [
                                            time,
                                            int(result['alliances']['blue']['score']),
                                            int(result['alliances']['red']['score']),
                                            result['event_key'],
                                            result['comp_level'],
                                            int(result['match_number'])
                                        ],
                                        firstTeam, 
                                        secondTeam, 
                                        year
                                   )
                                 )               
                else:
                    mainTeamAlliance = 'red'
                    matches.append( 
                                    MatchData(
                                        [
                                            time,
                                            int(result['alliances']['red']['score']), 
                                            int(result['alliances']['blue']['score']),
                                            result['event_key'],
                                            result['comp_level'],
                                            int(result['match_number'])
                                        ],
                                        firstTeam, 
                                        secondTeam, 
                                        year
                                    )
                                  )
                if winner=='none':
                    results['tie']=results['tie']+1
                elif winner==mainTeamAlliance:
                    results[firstTeam]=results[firstTeam]+1
                else:
                    results[secondTeam]=results[secondTeam]+1
        matches = sorted(matches)
    except Exception:
        print("Failed to get data for year "+str(year))
    return results, matches, year

def matchHappened(result):
    return result['alliances']['red']['score']!=-1 and result['alliances']['blue']['score']!=-1

def oppositeAlliances(result, firstTeam, secondTeam, color):
    return "frc"+str(secondTeam) in result['alliances'][color]['team_keys'] and "frc"+str(firstTeam) not in result['alliances'][color]['team_keys']