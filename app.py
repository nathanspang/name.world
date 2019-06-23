from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/createaccount')
def createaccount():
    return render_template('createaccount.html')

@app.route('/namegroup')
def namegroup():
    return render_template('namegroup.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)