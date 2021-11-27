import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    res = requests.get('https://news.ycombinator.com/news')
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.titlelink')
    votes = soup.select('.score')
    print(votes[0].get('id'))
