from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get('https://api.npoint.io/4a1750cd24eb61eb6cd9')
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:post_id>')
def get_single_post(post_id):
    response = requests.get('https://api.npoint.io/4a1750cd24eb61eb6cd9')
    all_posts = response.json()
    returned_post = {}
    for post in all_posts:
        if post['id'] == post_id:
            returned_post = post
    return render_template("post.html", post=returned_post)


if __name__ == "__main__":
    app.run(debug=True)
