from unicodedata import name
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def receive_data():
    username = request.form['username']
    password = request.form['password']
    return render_template('login.html', name=username, password=password)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
