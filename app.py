from flask import Flask, render_template, redirect
from flask.globals import request
from flask_debugtoolbar import DebugToolbarExtension

from Surveys import Question as Q, Survey as S, satisfaction_survey as ss, personality_quiz as pq, surveys

app = Flask(__name__)
app.config['SECRET_KEY'] = "himitsu-desu"

debug = DebugToolbarExtension(app)


responses = []


@app.route('/')
def start_survey():
    """Return start survery page."""
    
    title = ss.title
    instructions = ss.instructions
    
    return render_template("start.html", instructions = instructions, title = title)


@app.route('/question/<int:id>')
def question(id):
    """Return question page."""

    
    return render_template("question.html")
