import smtplib
from flask import Flask, render_template, request
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


@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    msg_send = None
    if request.method == 'GET':
        return render_template('contact.html', msg_send=False)
    else:
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template('contact.html', msg_send=True)


@app.route('/post/<int:id>')
def post_page(id):
    s_post = None
    for post in all_posts:
        if post['id'] == id:
            s_post = post
    return render_template('post.html', post=s_post)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login('my_email', 'my_password')
        connection.sendmail(email, 'boriskamtou@gmail.com', email_message)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
