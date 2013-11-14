# -*- coding: utf-8 -*-
"""
db2rest
~~~~~~~
A HTTP REST API for relational databases

:copyright: (c) 2013 by Functional Genomic Center Zurich, Nicola Palumbo.

:license: MIT, see LICENSE for more details.
"""
import os

module_dir = os.path.sep.join(__file__.split(os.path.sep)[:-1])
file_name = os.path.sep.join((module_dir, 'version.txt'))

def version():
    with open(file_name) as f:
        return f.read().strip()

def update_version(value):
    __version__ = value
    with open(file_name, 'w') as f:
        f.write(str(value))

__version__ = version()
del version

