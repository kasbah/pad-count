import os

def makedir(p):
    if not os.path.exists(p):
        os.makedirs(p)
