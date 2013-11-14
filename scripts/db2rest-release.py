#!/usr/bin/env python
import sys
import subprocess
import os
import db2rest

def main(vers):
    # TODO: Improve this script

    setup_dir  = os.path.sep.join(db2rest.__file__.split(os.path.sep)[:-2])
    setup_file = os.path.sep.join((setup_dir, 'setup.py'))
    module_dir = os.path.sep.join(db2rest.__file__.split(os.path.sep)[:-1])
    version_txt = os.path.sep.join((setup_dir, 'version.txt'))
    # Updating the setup.py
    db2rest.update_version(vers)
    
    print "Update the version!"
    subprocess.call(['git', 'add', version_txt])

    subprocess.call(['git', 'commit', '-m', 'Updated setup.py for RELEASE: version %s' % vers])
    print "Commited!"

    subprocess.call(['git', 'tag', '-a', 'v%s' % vers, '-m', 'RELEASE: %s' % vers])
    print "Tag created!"

    subprocess.call(['git', 'push', '--all'])
    print "Pushed!"


    print "Building gztar and zip"
    p = subprocess.Popen(["python", setup_file , "sdist", "--formats=gztar,zip", "upload"], cwd=setup_dir)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        vers = sys.argv[1]
        main(vers=vers)
    else:
        print "Specify the version!"
