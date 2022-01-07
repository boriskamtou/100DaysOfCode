import requests
from bs4 import BeautifulSoup
import smtplib

product_url = 'https://www.amazon.com/gp/product/B07X49967V/ref=ewc_pr_img_1?smid=ATVPDKIKX0DER&psc=1'
accept_language = 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,es-US;q=0.6,es;q=0.5'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'

headers_options = {
    'Accept-Language': accept_language,
    'User-agent': user_agent
}

response = requests.get(product_url, headers=headers_options)

amazon_webpage = response.text

soup = BeautifulSoup(amazon_webpage, 'lxml')

product_price = soup.find('span', class_='a-offscreen').getText()
price_without_currency = product_price.split('$')[1]
price = float(price_without_currency)

product_name = soup.find('span', class_='product-title-word-break').getText()

my_email = 'boriskamtou@gmail.com'

if 20 <= 30:
    with smtplib.SMTP('smtp.gmail.com') as connexion:
        connexion.starttls()
        connexion.login(user=my_email, password='')
        connexion.sendmail(msg=f'Subject: {product_name} is now {price}', from_addr=my_email,
                           to_addrs=my_email)
