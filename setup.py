# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

LONGDOC = """
lst

# or

lst.py
"""

setup(name = 'lst',
      version = '1.0.0',
      description = '',
      long_description = LONGDOC,
      author = 'cxl',
      author_email = 'i@cxl.im',
      url = 'https://github.com/imcxl/lst',
      license = 'MIT',
      install_requires = [],
      classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities'
      ],
      keywords = 'ls, lst',
      packages = find_packages('src'),
      package_dir = {'':'src'},
)
