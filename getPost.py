import requests
import json
from key import key

url = "http://api.letgo.com/api/iplookup.json"

r = requests.get(url)
print(r.status_code)
data = r.json()
print(type(data))

l1 = str(data['latitude'])
print(l1)
l2 = str(data['longitude'])
print(l2)


params = {'key': 'fa24d7edab6f43dd9864ee9d1dae84e5','q':(l1+","+l2)}
url3 = 'https://api.opencagedata.com/geocode/v1/json?language=en&pretty=1'
r2 = requests.get(url3,params= params)
print(r2.status_code)
print(r2.url)
print(type(r2))
z = r2.json()
print('\nAddress is : ',z['results'][0]['formatted'])
