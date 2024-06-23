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