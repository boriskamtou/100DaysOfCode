from flask import Flask, redirect, render_template, request, session, url_for
import sqlite3  # Pour utiliser un base de donnée SQlite
from flask_sqlalchemy import SQLAlchemy
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired
app = Flask(__name__)

# creation d'une connexion à la base de donnée
# Si elle n'existe pas elle sera crée
# db = sqlite3.connect("books-collection.db")

# Ensuite on crée un curseur pour manipuler notre bd | c'est un pointeur vers notre bd qui nous
# permet d'effectuer des opérations sur elle
# delete, add, update, read
# cursor = db.cursor()

# Creation de la table Book
# [execute] permett d'exécuter une action
# cursor.execute(
#     "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# Ajouter des données à notre BD
# cursor.execute(
#     "INSERT INTO books VALUES(1, 'Harry Poter', 'J. K Rowling', '9.3')")
# db.commit()

all_books = []


# Avec SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db = SQLAlchemy(app)


# Creation d'un table
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self) -> str:
        return '<Books %r>' % self.title


# initialisation de la base de données
db.create_all()

# Création d'un enregistrement
ztf_book = Books(title="Le chemin de la vie", author="Z. T. Fomun", rating=9.5)

# ajout de cet enregistrement à la base de données (CREATE)
db.session.add(ztf_book)
db.session.commit()

# Lire toutes les données en BD (READ)
all_books = session.query(Books).all()
# Lire une donnée spécifique en BD (READ)
filter_book = Books.query.filter_by(title='Harry Poter').first()


# Mise à jour d'un enregistrement particulier par recherche
book_to_update = Books.query.filter_by(title='Harry Poter').first()
book_to_update.title = "Harry Potter and the Chamber of Secrets"
db.session.commit()

# Mise à jour d'un enregistrement particulier par son ID
book_id = 1
book_to_update = Books.query.get(book_id)
book_to_update.title = "Un nouveau se lève"
db.session.commit()

# Supprimer un enregistrement par son ID
book_id = 1
book_to_delete = Books.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()


@app.route('/')
def index():
    return render_template('index.html', books=all_books)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book_name = request.form['book_name']
        book_author = request.form['book_author']
        rating = request.form['rating']
        new_book = {
            "title": book_name,
            "author": book_author,
            "rating": rating,
        }
        all_books.append(new_book)
        print(all_books)
        redirect(url_for('index'))
    return render_template('add.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
