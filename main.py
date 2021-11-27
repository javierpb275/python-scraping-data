import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    res = requests.get('https://news.ycombinator.com/news')
    print(res.text)
