from flask import Flask, render_template, request, Blueprint
import GraphGenerator

app = Flask(__name__)

views = Blueprint('views', __name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        team1=request.form.get('team1')
        team2=request.form.get('team2')
        try:
            team1 = int(team1)
            team2 = int(team2)
            info, path = GraphGenerator.getRecord(team1, team2)
            return render_template('index.html', haveContent=True, information=info, path=path, team1=str(team1), team2=str(team2))
        except Exception:
            return render_template('index.html', haveContent=False)
    return render_template('index.html', haveContent=False)

app.run(debug=False)