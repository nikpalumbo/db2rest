# -*- coding: utf-8 -*-
""" db2rest setup.py script """

# db2rest
from db2rest import __version__

# system
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from os.path import join, dirname

__version__ = "db2rest: 0.1.0:"
setup(
    name=__version__,
    version='0.1.0',
    description='A HTTP REST API for relational databases',
    author='Nicola Palumbo',
    author_email='nikpalumbo@gmail.com',
    packages=['db2rest','db2rest.test'],
    url='http://stephanepechard.github.com/projy',
    long_description=open('README.txt').read(),
    install_requires=['sqlalchemy','mysql-python','werkzeug',
                      'simplejson','jinja2','python-ldap'],
    test_suite='db2rest.test',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
      ],
)
