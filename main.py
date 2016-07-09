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

def run(pin_count):
    if os.path.exists('data/pdfs/{}'.format(pin_count)):
        uids = list_files('pdfs', pin_count)
    else:
        uids = octopart.get_pdfs('pdfs', pin_count)

    for uid in uids:
        image_folder = 'data/training/{}'.format(pin_count)
        rejected_uids_folder = 'data/rejected/uids/{}'.format(pin_count)
        rejected_sha_folder = 'data/rejected/sha/{}'.format(pin_count)
        utils.makedir(image_folder)
        utils.makedir(rejected_uids_folder)
        utils.makedir(rejected_sha_folder)

        output_path = '{}/{}.png'.format(image_folder, uid)
        rejected_uid_path = '{}/{}'.format(rejected_uids_folder, uid)

        if os.path.exists(output_path) or os.path.exists(rejected_uid_path):
            continue

        pdf_path = 'data/pdfs/{}/{}.pdf'.format(pin_count, uid)

        sha = sp.check_output(['sha1sum', pdf_path]).split(' ')[0]
        rejected_sha_path = '{}/{}'.format(rejected_sha_folder, sha)

        if os.path.exists(rejected_sha_path):
            continue

        evince = sp.Popen(['evince', pdf_path], stdout=sp.PIPE, stderr=sp.STDOUT)

        try:
            c = raw_input('{}> '.format(uid))
        except EOFError:
            c = 'e'

        if c == 's':
            #take a screenshot with imagemagick's import
            sp.check_call(['import', output_path])
        elif c == 'r':
            pass
        elif c == 'e':
            evince.kill()
            print("")
            sys.exit(0)
        elif c == 'n':
            sp.check_call(['touch', '{}/{}'.format(rejected_sha_folder, sha)])
        else:
            sp.check_call(['touch', rejected_uid_path])
        evince.kill()

run(4)
