from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class LogIn(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()])
    password = StringField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Log In')

class CreateAccount(FlaskForm):
    first_name = StringField('First Name: ', validators=[DataRequired()])
    last_name = StringField('Last Name: ', validators=[DataRequired()])
    username = StringField('Username: ', validators=[DataRequired()])
    aboutyou = TextAreaField('About you: ')
    password = StringField('Password: ', validators=[DataRequired()])
    confirm_pass = StringField('Confirm Password: ', validators=[DataRequired()])
    submit = SubmitField('Create Account')
