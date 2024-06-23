commands I ran to get request

```python
>>> import requests
>>> res = requests.get('https://www.weather.gov')
>>> type(res)
<class 'requests.models.Response'>
>>> len(res.text)
154569
>>> weather = open('Weather.html','wb')
>>> for chunk in res.iter_content('100000):
  File "<stdin>", line 1
    for chunk in res.iter_content('100000):
                                  ^
SyntaxError: unterminated string literal (detected at line 1)
>>> for chunk in res.iter_content(100000):  
...     weather.write(chunk)
...
100000
54569
>>> weather.close()
```
Always the small stuff that gets you

Activity 2 we ran:
```python
>>> res = requests.get('https://nostarch.com')    
>>> res.raise_for_status()
>>> res
<Response [200]>
>>> noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
>>> type(noStarchSoup)
<class 'bs4.BeautifulSoup'>

```
We also did the following:
```python
<class 'bs4.BeautifulSoup'>
>>> exampleFile = open('example.html')
>>> exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
>>> type(exampleSoup)
<class 'bs4.BeautifulSoup'>

```
Following this, we assigned the variable elems:
```python
>>> exampleFile = open('example.html')                                 
>>> exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
>>> elems = exampleSoup.select('#author') 
>>> type(elems)
<class 'list'>
>>> len(elems)
1
>>> type(elems[0])
<class 'bs4.element.Tag'>
>>> str(elems[0])
'<span id="author">Al Sweigart</span>'
>>> elems[0].getText()
'Al Sweigart'
>>> elems[0].attrs    
{'id': 'author'}

```
