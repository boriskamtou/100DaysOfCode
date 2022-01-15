from flask import Flask, render_template
from datetime import date
import requests

app = Flask(__name__)


@app.route('/')
def index():
    todays_date = date.today()
    year = todays_date.year
    return render_template('index.html', y=year)


@app.route('/guess/<name>')
def guess(name):
    response = requests.get(f'https://api.genderize.io?name={name}')
    data = response.json()
    return render_template('genderize.html', result=data)


@app.route('/blog')
def get_blog():
    response = requests.get('https://api.npoint.io/d43bddc349de54d4844c')
    all_post = response.json()
    return render_template('blog.html', posts=all_post)


if __name__ == '__main__':
    app.run(debug=True)
