from flask import Flask, render_template, redirect
from flask.globals import request
from flask_debugtoolbar import DebugToolbarExtension

from Surveys import Question as Q, Survey as S, satisfaction_survey as ss, personality_quiz as pq, surveys
from QuestionForm import QuestionForm as QF


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
    form = QF()

    current_id = len(responses)
    title = ss.title
    question = ss.questions[current_id].question
    choices = ss.questions[current_id].choices
    instructions = ss.instructions

    if id == current_id:
        return render_template("question.html", question = question, title = title, id = current_id, form = form, instructions = instructions, choices = choices)
    else: 
        return redirect(f'/question/{current_id}')
        # redirect(f'/question/{current_id}', q = question, title = title, id = current_id, form = form, instructions = instructions)
