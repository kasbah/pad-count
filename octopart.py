import json
import urllib
import os

from apikey import apikey

url = 'http://octopart.com/api/v3/parts/search?'
url += '&q=SOIC'
url += '&limit=100'
url += '&apikey={}'.format(apikey)
url += '&include[]=datasheets'
url += '&include[]=specs'

data = urllib.urlopen(url).read()
response = json.loads(data)

# print mpn's
for result in response['results']:
    part = result['item']
    sheets = part['datasheets']
    if len(sheets) > 0:
        url = None
        for sheet in sheets:
            if 'url' in sheet:
                if os.path.splitext(sheet['url'])[-1] == '.pdf':
                    url = sheet['url']
                    break
        if url is not None:
            specs = part['specs']
            if 'pin_count' in specs:
                n_pins = specs['pin_count']['display_value']
                print n_pins
