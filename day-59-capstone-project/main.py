from flask import Flask, render_template
import requests
app = Flask(__name__)

data = requests.get('https://api.npoint.io/a1dc60176ce39eae1436')
all_posts = data.json()


@app.route('/')
def index():
    return render_template('index.html', posts=all_posts)


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


@app.route('/post/<int:id>')
def post_page(id):
    s_post = None
    for post in all_posts:
        if post['id'] == id:
            s_post = post
    return render_template('post.html', post=s_post)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
