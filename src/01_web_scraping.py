import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import pandas as pd

base_url = 'http://en.people.cn/202936/'

begin = 74
end = begin + 10

for page_idx in range(begin, end):
    url = f'http://en.people.cn/202936/index{page_idx}.html'
    page = requests.get(url)
    page.encoding = 'utf-8'
    news_list = BeautifulSoup(page.text, 'html.parser')

    ul = news_list.find('ul', class_='foreign_list8 cf')
    list_items = ul.find_all('li')

    data = []

    for item in list_items:
        title = item.find('a').text.strip()
        date = item.find('span').text.split(' ')[0]
        absolute_url = urljoin(base_url, item.find('a')['href'])
        response = requests.get(absolute_url)
        article_soup = BeautifulSoup(response.content, 'html.parser')
        article_div = article_soup.find('div', class_='w860 d2txtCon cf')

        if article_div is not None:
            article = article_div.text.strip()
        else:
            print(f"Skipping article {title} - no article text found")

        data.append([title, date, absolute_url, article])
        

    print(f"Page {page_idx} : {len(data)} news Save")
    df = pd.DataFrame(data, columns=['Title', 'Date', 'URL', 'Article'])
    df.to_csv(f'../data/raw/news_page_{page_idx}.csv', index=False)
    print("------------------")

