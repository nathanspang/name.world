from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class LogIn(FlaskForm):
    username = StringField('Username: ')
    password = StringField('Password: ')
    submit = SubmitField('Log In')
