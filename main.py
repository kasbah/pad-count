import subprocess as sp
import time
import os
import sys

import utils
import octopart

def list_files(prefix, pin_count):
    uids = []
    paths = os.listdir('data/{}/{}'.format(prefix, pin_count))
    for path in paths:
        uids.append(os.path.splitext(os.path.basename(path))[0])
    return uids

if os.path.exists('data/pdfs'):
    uids = list_files('pdfs', 4)
else:
    uids = octopart.get_pdfs('pdfs', 4)

for uid in uids:
    image_folder = 'data/training/4'
    rejected_folder = 'data/rejected/uids/4'
    utils.makedir(image_folder)
    utils.makedir(rejected_folder)

    output_path = '{}/{}.png'.format(image_folder, uid)
    rejected_path = 'data/rejected/{}'.format(uid)

    if os.path.exists(output_path) or os.path.exists(rejected_path):
        continue

    evince = sp.Popen(['evince', 'data/pdfs/4/{}.pdf'.format(uid)], stdout=sp.PIPE)

    try:
        c = raw_input('{}> '.format(uid))
    except EOFError:
        c = 'e'

    if c == 's':
        #take a screenshot with imagemagick
        sp.check_call(['import', output_path])
    elif c == 'r':
        pass
    elif c == 'e':
        evince.kill()
        print("")
        sys.exit(0)
    else:
        sp.check_call(['touch', rejected_path])

    evince.kill()
