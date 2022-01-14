from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world 2.0!'


@app.route('/username/<name>')
def greet_user(name):
    return f'Hello {name}!'


if __name__ == '__main__':
    app.run()
