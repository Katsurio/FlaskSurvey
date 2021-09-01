from flask import Flask, render_template, redirect, flash
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
    """Return start survey page."""
    
    title = ss.title
    instructions = ss.instructions
    
    return render_template("start.html", instructions = instructions, title = title)


@app.route('/question/<int:id>')
def question(id):
    """Return question page."""
    form = QF()

    current_id = len(responses)
    
    if id == current_id:
        title = ss.title
        question = ss.questions[current_id].question
        choices = ss.questions[current_id].choices
        instructions = ss.instructions
        return render_template("question.html", question = question, title = title, id = current_id, form = form, instructions = instructions, choices = choices)
    elif id > len(ss.questions) and len(responses) >= len(ss.questions):
        return redirect('/thanks')
    else: 
        flash("Invalid question, try again!", 'warn')
        return redirect(f'/question/{current_id}')


@app.route('/answer', methods=['POST'])
def handle_answer():
    """Handle answer from form submission and redirect."""
    
    answer = request.form['choices']
    responses.append(answer)
    current_id = len(responses)
    
    if len(responses) < len(ss.questions):
        return redirect(f'/question/{current_id}')
    else:
        return redirect('/thanks')
    
    
@app.route('/thanks')
def thanks():
    """Return thank you page."""
    
    return render_template("thanks.html")