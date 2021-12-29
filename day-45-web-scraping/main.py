from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/newest')

ny_webpage = response.text

soup = BeautifulSoup(ny_webpage, 'html.parser')
articles = soup.find_all('a', class_='titlelink')

article_texts = []
article_links = []

for article in articles:
    text = article.getText()
    article_texts.append(text)
    link = article.get('href')
    article_links.append(link)


article_upvote = [int(score.getText().split()[0]) for score in soup.find_all('span', class_='score')]

largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)


print(article_texts[largest_index])
print(article_links[largest_index])


# with open('website.html', encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title.string)
