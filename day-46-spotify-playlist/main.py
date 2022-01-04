from bs4 import BeautifulSoup
import requests
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

SPOTIPY_CLIENT_ID = 'eb13e4b9ba0248eea04be77abe252af1'
SPOTIPY_CLIENT_SECRET = '098a63377c104154bf56acc61acfa515'
SPOTIPY_REDIRECT_URI = 'http://example.com'
SPOTIPY_SCOPE = "playlist-modify-private",
URL = 'http://example.com/?code=AQCKhbDlKK62Lt0Z3ClOP-gRJQwryavFViy_QrLP2MxPka2rljHZMcdxI-mD588DuQ8fjv6yNZCQENrkmdH9ogIMQ0hk3rmc9h0WKnG7ksmA5XfqSOXNYPmFHHONBAwuUzppgOzSXabUSdUXaWlfdJfebXDpQQ714F-btu7h5xvR8_x8hYXfILOnPktaqOM'

date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')

response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}')
billboard_webpage = response.text

soup = BeautifulSoup(billboard_webpage, 'html.parser')

all_titles = soup.find_all(name='h3', class_='u-max-width-230@tablet-only')

titles = []

for title in all_titles:
    text = title.getText()
    new_text = re.sub('\n+', '', text)
    titles.append(new_text)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=SPOTIPY_SCOPE,
        cache_path="token.txt",
        show_dialog=True, ), )

current_user_id = sp.current_user()['id']

song_uris = []
year = date.split("-")[0]
for title in titles:
    result = sp.search(q=f'track:{title} year:{date}', type='track')
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{title} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=current_user_id, name=f"{date} Billboard 100", public=False)

sp.user_playlist_add_tracks(user=current_user_id, playlist_id=playlist["id"], tracks=song_uris)
