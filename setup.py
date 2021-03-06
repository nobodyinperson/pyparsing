#!/usr/bin/env python

"""Setup script for the pyparsing module distribution."""

import sys
from setuptools import setup
from pyparsing import __version__ as pyparsing_version

modules = ["pyparsing",]

setup(# Distribution meta-data
    name = "python3-pyparsing" if sys.argv[1] == "bdist_rpm" else "pyparsing",
    version = pyparsing_version,
    description = "Python parsing module",
    author = "Paul McGuire",
    author_email = "ptmcg@users.sourceforge.net",
    url = "https://github.com/pyparsing/pyparsing/",
    download_url = "https://pypi.org/project/pyparsing/",
    license = "MIT License",
    py_modules = modules,
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        ]
    )
