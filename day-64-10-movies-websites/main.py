from xml.dom import ValidationErr
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie.db'
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
db = SQLAlchemy(app)

API_KEY = 'bcb184a317335ad93da00f543ab44f04'


def rating_validator(form, field):
    if field.data > 10:
        raise ValidationErr('You cannot exced 10')
    else:
        raise ValidationErr('You cannot go less than 0')


class RateMovieForm(FlaskForm):
    rating = FloatField(label='Your rating out of 10 e.g 7.5',
                        validators=[rating_validator])
    review = StringField(label='Your Review')
    submit = SubmitField(label='Done')


class AddMovieForm(FlaskForm):
    title = StringField(label='Movie title', validators=[DataRequired()])
    submit = SubmitField(label='Add Movie')


all_movies = []

movies_data = []

# Creation de la table des Movies


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    year = db.Column(db.Integer)
    description = db.Column(db.String(250))
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String, nullable=False)

    def __repr__(self) -> str:
        return '<Movie %r>' % self.title


# Creation de la BD
db.create_all()


@app.route("/")
def index():
    all_movies = Movie.query.all()
    movie_selected_id = request.args.get('id')
    if movie_selected_id != None:
        response = requests.get(
            f'https://api.themoviedb.org/3/movie/{movie_selected_id}?api_key={API_KEY}&language=en-US')
        movie_data = response.json()
        print(movie_data)
        poster_path = movie_data['poster_path']
        new_movie = Movie(
            title=movie_data['title'],
            year=movie_data['release_date'].split('-')[0],
            description=movie_data['overview'],
            rating=10,
            ranking=8,
            review='A review',
            img_url=f'https://api.themoviedb.org/{poster_path}'
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("index.html", movies=all_movies)


@app.route('/add', methods=['GET', 'POST'])
def add():
    add_movie_form = AddMovieForm()
    # Get movies by title
    if request.method == 'POST':
        title = add_movie_form.title.data
        response = requests.get(
            f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={title}&page=1')
        data = response.json()
        movies_data = data['results']
        return render_template('select.html', movies=movies_data)
    return render_template('add.html', form=add_movie_form)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    rate_movie_form = RateMovieForm()
    movie_id = request.args.get('id')
    movie_to_update = Movie.query.get(movie_id)
    if request.method == 'POST':
        movie_to_update.rating = rate_movie_form.rating.data
        movie_to_update.review = rate_movie_form.review.data
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', movie=movie_to_update, form=rate_movie_form)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
