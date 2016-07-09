import subprocess
import time
import os

import utils
import octopart

def list_files(prefix, pin_count):
    uids = []
    paths = os.listdir('data/{}/pdfs/{}'.format(prefix, pin_count))
    for path in paths:
        uids.append(os.path.splitext(os.path.basename(path))[0])
    return uids

if os.path.exists('data'):
    uids = list_files('training', 4)
else:
    uids = octopart.get_pdfs('training', 4)

for uid in uids[:2]:
    image_folder = 'data/training/images/4'
    utils.makedir(image_folder)
    subprocess.Popen(['scrot', '-s', '{}/{}.png'.format(image_folder, uid)])
    subprocess.check_output(['evince', 'data/training/pdfs/4/{}.pdf'.format(uid)])
    time.sleep(0.1)
