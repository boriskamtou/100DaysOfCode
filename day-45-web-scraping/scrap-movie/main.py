import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')

movie_webpage = response.text

soup = BeautifulSoup(movie_webpage, 'html.parser')

list_of_movies_title = soup.find_all(name='h3', class_='title')

movies_titles = [movie.getText() for movie in list_of_movies_title]
movies = movies_titles[::-1]

with open("movies.txt", mode='w') as file:
    for movie in movies:
        file.write(f"{movie}\n")
