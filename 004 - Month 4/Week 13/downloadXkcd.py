#! python3
#       downloadXkcd.py - Downloads every SINGLE XKCD comic (Prep your HD)
#       an ATBS Program | Chapter 12 Project 2

import requests
import os
import bs4


url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True) # call os.makedir to make sure folder exists
while not url.endswith('#'):
    # download page
    print('Downloading page %s... ' % url)
    res = requests.get(url)
    res.raise_for_status()                                     # Checks for status (200)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')  # Same code as before

    # find url
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        # download image
        print('Downloading image %s... ' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
    # save the image to ./xkcd.
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')

    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    # get the previous button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done.')
