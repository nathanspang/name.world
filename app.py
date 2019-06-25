from flask import Flask, render_template
from login import LogIn
from createaccount import CreateAccount

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = False
    password = False

    form = LogIn()
    if form.validate_on_submit():
        username = form.username.data
        form.username.data = ''

        password = form.password.data
        form.password.data = ''

    return render_template('login.html', form=form, username=username, password=password)

@app.route('/createaccount', methods=['GET', 'POST'])
def createaccount():
    first_name = False
    last_name = False
    username = False
    password = False
    confirm_pass = False

    form = CreateAccount()

    if form.validate_on_submit():
        first_name = form.first_name.data
        form.first_name.data = ''

        last_name = form.last_name.data
        form.last_name.data = ''

        username = form.username.data
        form.username.data = ''

        password = form.password.data
        form.password.data = ''

        confirm_pass = form.confirm_pass.data
        form.confirm_pass.data = ''

    return render_template('createaccount.html', form=form, first_name=first_name, 
    last_name=last_name, username=username, password=password, confirm_pass=confirm_pass)

@app.route('/namegroup')
def namegroup():
    return render_template('namegroup.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)