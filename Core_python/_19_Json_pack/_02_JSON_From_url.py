import json
from urllib.request import urlopen

with open("https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=EUR=json") as response:
    source = response.read()
    print(source)
    
print(source)


import requests

x = requests.get('https://api.publicapis.org/entries')
print(x.text)
