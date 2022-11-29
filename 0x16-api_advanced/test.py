#!/usr/bin/python3
import requests

auth = requests.auth.HTTPBasicAuth('7zwrg7KHpgoa49qJ89CELQ', 'MqWWvd3LiAPR8bYDGnCFGxaARZGv7g')
data = {'grant_type': 'password',
        'username': 'alxreezy',
        'password': 'Alxtest1'}
headers = {'User-Agent': 'MyBot/0.0.1'}
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)
TOKEN = res.json()['access_token']
parms = {'limit': 10}
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
response = requests.get('https://oauth.reddit.com/r/programming/top', headers=headers, params=parms)
results = response.json().get("data")
[print(c.get("data").get("title")) for c in results.get("children")]
