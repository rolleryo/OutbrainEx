### OutRain Exercise ###

import requests #http://docs.python-requests.org/en/latest/
from requests import get
import ipinfo # get ip based location

# get external ip using http request from ipify
external_ip = get('https://api.ipify.org').content.decode('utf8')

# get city & country according to external ip using ipinfo library
ipinfo_token = 'd5a13af3bebba0'
handler = ipinfo.getHandler(ipinfo_token) # create object handler 
ipinfo_details = handler.getDetails(external_ip) # use getDetails property
city = ipinfo_details.city
country = ipinfo_details.country
print("City:"+city+" Country "+country)