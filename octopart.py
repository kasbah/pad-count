import json
import urllib

from apikey import apikey

url = 'http://octopart.com/api/v3/parts/search?'
url += '&q=SOIC'
url += '&limit=100'
url += '&apikey={}'.format(apikey)
url += '&include[]=datasheets'

data = urllib.urlopen(url).read()
response = json.loads(data)

# print mpn's
for result in response['results']:
    part = result['item']
    sheets = part['datasheets']
    if len(sheets) > 0:
        print sheets[0]['url']
