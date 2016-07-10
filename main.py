import subprocess as sp
import time
import os
import sys
import pickle

import utils
import octopart

pickle_path = "rejected.pickle"
if os.path.exists(pickle_path):
    with open(pickle_path, "rb") as f:
        rejected = pickle.load(f)
else:
    rejected = {
        "global": []
        , 2: []
        , 3: []
        , 4: []
        , 5: []
        , 6: []
        , 7: []
        , 8: []
    }


def write_state():
    with open(pickle_path, "w") as f:
        pickle.dump(rejected, f)


def path_to_uid(path):
    return os.path.splitext(os.path.basename(path))[0]


def uid_to_image(pin_count, uid):
    return 'data/training/{}/{}.png'.format(pin_count, uid)


def get_valid(pin_count, parts):
    valid = []
    for obj in parts:
        path = obj['path']
        uid = path_to_uid(path)
        if not os.path.exists(uid_to_image(pin_count, uid)):
            sha = sp.check_output(['sha1sum', path]).split(' ')[0]
            if (sha not in rejected[pin_count]) and (sha not in rejected['global']):
                valid.append(obj)
    return valid



def get_fresh_pdfs(pin_count, quota):
    valid = []
    i = 0
    while len(valid) < quota:
        parts = octopart.get_pdfs(pin_count, i)
        i += 1
        valid.extend(get_valid(pin_count, parts))
    return valid



def run(pin_count, quota):
    parts = get_fresh_pdfs(pin_count, quota)
    for obj in parts[0:quota]:
        pdf_path = obj['path']
        uid = path_to_uid(pdf_path)
        evince = sp.Popen(['evince', pdf_path], stdout=sp.PIPE, stderr=sp.STDOUT)

        def finish():
            write_state()
            evince.kill()

        try:
            c = raw_input('{}> '.format(obj['mpn']))
        except EOFError:
            c = 'e'

        if c == 's':
            path = uid_to_image(pin_count, uid)
            utils.makedir(os.path.dirname(path))
            #take a screenshot with imagemagick's import
            sp.check_call(['import', path])
        elif c == 'e':
            print("")
            finish()
            sys.exit(0)
        elif c == 'r':
            sha = sp.check_output(['sha1sum', pdf_path]).split(' ')[0]
            print('rejecting sha1 for pin_count of {}: {}'.format(pin_count, sha))
            rejected[pin_count].append(sha)
        else:
            sha = sp.check_output(['sha1sum', pdf_path]).split(' ')[0]
            print('rejecting sha1: {}'.format(sha))
            rejected['global'].append(sha)
        finish()



run(int(sys.argv[1]), int(sys.argv[2]))
