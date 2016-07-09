import json
import urllib
import os

from apikey import apikey

def makedir(p):
    if not os.path.exists(p):
        os.makedirs(p)

def get_pdfs(pin_count, offset=0):
    makedir('pdfs/{}'.format(pin_count))
    url = 'https://octopart.com/api/v3/parts/search?'
    url += '&q='
    url += '&filter[fields][specs.pin_count.value][]={}'.format(pin_count)
    url += '&start={}'.format(offset * 100)
    url += '&limit=100'
    url += '&apikey={}'.format(apikey)
    url += '&include[]=datasheets'
    url += '&include[]=specs'

    data = urllib.urlopen(url).read()
    response = json.loads(data)

    uids = []
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
                uid = part['uid']


get_pdfs(2)
