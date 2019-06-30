import os
from flask import Flask, render_template, session, redirect, url_for, flash
from forms import LogIn, CreateAccount
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisfornow'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)
Migrate(app, db)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = False
    password = False

    form = LogIn()
    if form.validate_on_submit():
        session['username'] = form.username.data
        session['password'] = form.password.data
        flash(f'Thank you, Login Successful!')
        return redirect(url_for('namegroup'))

    return render_template('login.html', form=form, username=username, password=password)

@app.route('/createaccount', methods=['GET', 'POST'])
def createaccount():
    first_name = False
    last_name = False
    username = False
    aboutyou = False
    password = False
    confirm_pass = False

    form = CreateAccount()

    if form.validate_on_submit():
        session['first_name'] = form.first_name.data
        session['last_name'] = form.last_name.data
        session['username'] = form.username.data
        session['aboutyou'] = form.aboutyou.data
        session['password'] = form.password.data
        session['confirm_pass'] = form.confirm_pass.data
        flash(f'Thank you, Account Created! Please Log in to continue: ')
        return redirect(url_for('login'))

    return render_template('createaccount.html', form=form, first_name=first_name, 
    last_name=last_name, username=username, aboutyou=aboutyou, password=password, confirm_pass=confirm_pass)

@app.route('/namegroup')
def namegroup():
    return render_template('namegroup.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)