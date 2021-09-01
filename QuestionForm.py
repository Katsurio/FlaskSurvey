from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired
from Surveys import satisfaction_survey as ss

class QuestionForm(FlaskForm):
    place = StringField('Place:', validators=[DataRequired()])
    radio = RadioField('Choices', choices=[], validators=[DataRequired()])
    submit = SubmitField('Submit')
    