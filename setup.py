#!/usr/bin/env python

from io import open
from setuptools import setup

"""
:authors: borry-dev
:license: MIT License
:copyright: (c) 2021 borry-dev
"""

version = '1.4'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='randomidentity',
    version=version,

    author='borry-dev',

    description=(
        u'Python module for writing scripts for project management platform '
        u'Club House (clubhouse.io API wrapper)'
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/borry-dev/randomidentity',
    download_url='https://github.com/borry-dev/randomidentity/archive/main.zip',

    license='MIT License',

    packages=['randomidentity'],
    install_requires=['random'],

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)