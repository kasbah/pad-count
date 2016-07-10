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

def run(pin_count, quota=10):
    if os.path.exists('data/pdfs/{}'.format(pin_count)):
        uids = list_files('pdfs', pin_count)
    else:
        uids = octopart.get_pdfs(pin_count, quota)

    image_folder = 'data/training/{}'.format(pin_count)
    rejected_sha_global_folder = 'data/rejected/sha/global'
    rejected_sha_local_folder = 'data/rejected/sha/{}'.format(pin_count)
    utils.makedir(image_folder)
    utils.makedir(rejected_sha_global_folder)
    utils.makedir(rejected_sha_local_folder)

    for uid in uids:

        output_path = '{}/{}.png'.format(image_folder, uid)

        if os.path.exists(output_path):
            print('ignoring existing uid {}'.format(uid))
            continue

        pdf_path = 'data/pdfs/{}/{}.pdf'.format(pin_count, uid)
        sha = sp.check_output(['sha1sum', pdf_path]).split(' ')[0]
        rejected_sha_global_path = '{}/{}'.format(rejected_sha_global_folder, sha)
        rejected_sha_local_path = '{}/{}'.format(rejected_sha_local_folder, sha)

        if os.path.exists(rejected_sha_global_path) or os.path.exists(rejected_sha_local_path):
            print('ignoring rejected sha1 {}'.format(sha))
            continue

        evince = sp.Popen(['evince', pdf_path], stdout=sp.PIPE, stderr=sp.STDOUT)

        try:
            c = raw_input('{}> '.format(uid))
        except EOFError:
            c = 'e'

        if c == 's':
            #take a screenshot with imagemagick's import
            sp.check_call(['import', output_path])
        elif c == 'e':
            evince.kill()
            print("")
            sys.exit(0)
        elif c == 'r':
            print('rejecting sha1 for pin_count of {}: {}'.format(pin_count, sha1))
            sp.check_call(['touch', rejected_sha_local_path])
        else:
            print('rejecting sha1: {}'.format(sha))
            sp.check_call(['touch', rejected_sha_global_path])
        evince.kill()

run(4)
