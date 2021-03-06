import json
import urllib
import os
import time

import utils

#to use this, make an apikey.py file with apikey variable assigned to your octopart apikey
from apikey import apikey

def get_100_pdfs(prefix, pin_count, offset=0):
    url = 'https://octopart.com/api/v3/parts/search?'
    url += '&q='
    url += '&filter[fields][specs.pin_count.value][]={}'.format(pin_count)
    url += '&filter[fields][specs.mounting_style.value][]=Surface Mount'
    url += '&start={}'.format(offset * 100)
    url += '&limit=100'
    url += '&apikey={}'.format(apikey)
    url += '&include[]=datasheets'
    url += '&include[]=specs'

    data = urllib.urlopen(url).read()
    response = json.loads(data)

    paths = []
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
                path = 'data/{}/{}/{}.pdf'.format(prefix, pin_count, uid)
                if not os.path.exists(path):
                    data = urllib.urlopen(url).read()
                    with open(path, 'w') as outfile:
                        outfile.write(data)
                paths.append({'mpn': part['mpn'], 'path': path})
    return paths



def get_pdfs(pin_count, i):
    utils.makedir('data/pdfs/{}'.format(pin_count))
    paths = get_100_pdfs('pdfs', pin_count, i)
    time.sleep(0.33)
    return paths
