import requests
from bs4 import BeautifulSoup
import lxml
import fake_useragent

for i in (1, 10):
    url = 'https://kups.club/?page=1'

    headers = {'user-agent': fake_useragent.UserAgent().random}

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')
    products = soup.find_all("div", class_='col-lg-4 col-md-4 col-sm-6 portfolio-item')
    for product in products:
        title_product = product.find("h3", class_='card-title')
        price_product = product.find('p', class_='card-text')
        print(title_product.text)
        print(price_product.text)
