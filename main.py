from flask import Flask, render_template, request, Blueprint, redirect, url_for
import GraphGenerator

app = Flask(__name__)

views = Blueprint('views', __name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        team1=request.form.get('team1')
        team2=request.form.get('team2')
        return redirect(url_for('custom', team1=team1, team2=team2))
    return render_template('index.html', haveContent=False)

@app.route('/<team1>vs<team2>', methods=['GET', 'POST'])
def custom(team1, team2):
    if request.method == 'POST':
        team1=request.form.get('team1')
        team2=request.form.get('team2')
        return redirect(url_for('custom', team1=team1, team2=team2)) 
    try:
        info, graph_url = GraphGenerator.getRecord(team1, team2)
        return render_template('index.html', haveContent=True, information=info, team1=str(team1), team2=str(team2), graph_url=graph_url)
    except:
        return render_template('index.html', haveContent=False)

app.run(debug=False)