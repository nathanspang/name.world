from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class CreateAccount(FlaskForm):
    first_name = StringField('First Name: ')
    last_name = StringField('Last Name: ')
    username = StringField('Username: ')
    password = StringField('Password: ')
    confirm_pass = StringField('Confirm Password: ')
    submit = SubmitField('Create Account')