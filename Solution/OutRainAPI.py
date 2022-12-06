### OutRain Exercise ###

import requests #http://docs.python-requests.org/en/latest/
from requests import get

### get external ip using http request from ipify
external_ip = get('https://api.ipify.org').content.decode('utf8')
print(external_ip)