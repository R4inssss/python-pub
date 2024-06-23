#! python3
#       searchpypi.py | Opens several search results
#       ATBS | Chapter 12 Program 1

import requests
import sys
import webbrowser
import bs4


# Then I created a search url variable for better readability, as well as understanding
def pypi_search(search_term):
    print('Searching pypi...')
    search_pypi = f'https://pypi.org/search/?q={search_term}'
    response = requests.get(search_pypi)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    linkElems = soup.select('.package-snippet')

    numOpen = min(5, len(linkElems))
    for i in range(numOpen):
        urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
        print('Opening', urlToOpen)
        webbrowser.open(urlToOpen)


def google_search(search_term):
    print('Searching Google...')
    search_google = f'https://google.com/search?q={search_term}'
    response = requests.get(search_google)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    linkElems = soup.select('div.g')  # I can't seem to find the right selector for Google hahaha

    numOpen = min(5, len(linkElems))
    for i in range(numOpen):
        urlToOpen = linkElems[i].get('href')
        if urlToOpen.startswith('/url?q='):  # Extract the actual URL from the result
            urlToOpen = urlToOpen.split('&')[0].replace('/url?q=', '')
            print('Opening', urlToOpen)
            webbrowser.open(urlToOpen)


# Removed failsafe since input has to be validated below:

# if len(sys.argv) > 1:
#     search_term = ' '.join(sys.argv[1:])
# else:
#     print("Please enter a search term")
#     sys.exit()

# left this the same

print('Would you like to search on google or pypi? (1 or 2)')
answer = input('>>> ')
if answer == '1':
    search_term = input('Enter what you want to Google: ')
    google_search(search_term)
elif answer == '2':
    search_term = input('Enter what you want to Pypi: ')
    pypi_search(search_term)
else:
    print('Please enter either 1 or 2')
    sys.exit()
