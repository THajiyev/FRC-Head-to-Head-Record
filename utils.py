from functools import total_ordering

time_constant = 9999999999999

@total_ordering
class MatchData():

    def __init__(self, data_list, team1, team2, year):
        self.time=data_list[0]
        self.firstTeamScore = str(data_list[1])
        self.secondTeamScore = str(data_list[2])
        self.year = year
        self.firstTeam = team1
        self.secondTeam = team2
        self.comp = data_list[3]
        self.level = data_list[4]
        self.matchNumber = int(data_list[5])

    def __lt__(self, obj):
        if self.time!=time_constant or obj.time!=time_constant:
            return ((self.time) < (obj.time))
        elif self.comp!=obj.comp:
            return self.comp<obj.comp
        else:
            if self.level==obj.level:
                return self.matchNumber<obj.matchNumber
            else:
                levels = ["qm","qf","sf","f"]
                return levels.index(self.level)<levels.index(obj.level)
  
    def __gt__(self, obj):
        if self.time!=time_constant or obj.time!=time_constant:
            return ((self.time) > (obj.time))
        elif self.comp!=obj.comp:
            return self.comp>obj.comp
        else:
            if self.level==obj.level:
                return self.matchNumber>obj.matchNumber
            else:
                levels = ["qm","qf","sf","f"]
                return levels.index(self.level)>levels.index(obj.level)
  
    def __eq__(self, obj):
        return False