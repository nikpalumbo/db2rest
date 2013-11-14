#!/usr/bin/env python
import sys
import subprocess
import os
import db2rest

def main():

    print "Building gztar and zip"
    setup_dir = os.path.sep.join(db2rest.__file__.split(os.path.sep)[:-2])
    setup_file = os.path.sep.join((setup_dir, 'setup.py'))
    p = subprocess.Popen(["python", setup_file , "sdist", "--formats=gztar,zip", "upload"], cwd=setup_dir)
    p.communicate()

if __name__ == '__main__':
    main()
