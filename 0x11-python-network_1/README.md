# Python - Network #1 — Alx System Engineering DevOps
0x11. Python - Network #1

```Python```
```Scripting```
```Back-end```
```API```

# Introduction

This README provides a simple guide on fetching internet resources using Python packages ``urllib`` and ``requests package``. These packages are commonly used for making HTTP requests and handling responses.

## urllib Python package

The urllib Python package provides a collection of modules for working with URLs. It includes functionality for making HTTP requests, handling cookies, and parsing URLs.

### How to fetch internet resources with the Python package urllib

```python
import urllib.request

# Fetching a webpage
with urllib.request.urlopen('https://www.elouardy.com') as response:
    html = response.read()
    print(html)
```

## How to decode urllib body response
```python
import urllib.request

response = urllib.request.urlopen('https://www.elouardy.com')
html = response.read().decode('utf-8')
print(html)
```

## requests Python package
The requests Python package is a user-friendly HTTP library for making requests and handling responses. It provides a higher-level interface compared to urllib.

## How to use the Python package requests
```python
import requests

# Fetching a webpage
response = requests.get('https://www.elouardy.com')
print(response.text)
```

## How to make HTTP GET request
```python
import requests

# GET request
response = requests.get('https://api.elouardy.com/data')
print(response.json())
```

## How to make HTTP POST/PUT/etc. request
```python
import requests

# POST request
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://api.elouardy.com/post', data=payload)

# PUT request
response = requests.put('https://api.elouardy.com/put', data=payload)
```

## How to fetch JSON resources
```python
import requests

response = requests.get('https://api.elouardy.com/data.json')
data = response.json()
print(data)
```

## How to manipulate data from an external service
```python
import requests

response = requests.get('https://api.elouardy.com/data')
data = response.json()

# Manipulate data as needed
for item in data['items']:
    print(item['name'])
```


## Contact Me
**Email:** ouadia@elouardy.com \
**Twitter:** https://twitter.com/_ELOUARDY
