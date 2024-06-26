#! python3
#       searchpypi.py | Opens several search results
#       ATBS | Chapter 12 Program 1

import requests
import sys
import webbrowser
import bs4

print('Searching...')
res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q=' + ' ' .join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('.package-snippet')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)

# Funny, because this program does NOT work for me on my initial encounter
