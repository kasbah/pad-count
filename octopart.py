import json
import urllib

from apikey import apikey

url = 'http://octopart.com/api/v3/parts/match?'
url += '&queries=[{"mpn":"SN74S74N"}]'
url += '&apikey={}'.format(apikey)

data = urllib.urlopen(url).read()
response = json.loads(data)

# print request time (in milliseconds)
print response['msec']

# print mpn's
for result in response['results']:
    for item in result['items']:
        print item.keys()
