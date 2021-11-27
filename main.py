import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    res = requests.get('https://news.ycombinator.com/news')
    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup.find('div'))
