import json
import urllib
import os

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
        url = sheets[0]['url']
        if os.path.splitext(url)[-1] == '.pdf':
            print url
