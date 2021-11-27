import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    res = requests.get('https://news.ycombinator.com/news')
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.titlelink')
    votes = soup.select('.score')
    print(votes[0].get('id'))

    def create_custom_hn(links, votes):
        hn = []
        for idx, item in enumerate(links):
            title = links[idx].getText()
            href = links[idx].get('href', None)
            points = int(votes[idx].getText().replace(' points', ''))
            print(points)
            hn.append({'title': title,'link':href})
        return hn

    print(create_custom_hn(links, votes))
