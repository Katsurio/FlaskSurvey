from flask import Flask, render_template, redirect
from flask.globals import request
from flask_debugtoolbar import DebugToolbarExtension

from Surveys import Question as Q, Survey as S, satisfaction_survey as ss, personality_quiz as pq, surveys

app = Flask(__name__)
app.config['SECRET_KEY'] = "himitsu-desu"

debug = DebugToolbarExtension(app)


@app.route('/')
def start_survey():
    """Return start survery page."""

    
    return render_template("start.html")