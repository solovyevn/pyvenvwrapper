#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pyvenvwrapper setup module"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as readme:
    long_description = readme.read()

setup(
    name='pyvenvwrapper',
    version='0.1.0',
    description='pyvenvwrapper is a small and lightweight set of Bash script functions, that enhance the use of Python pyvenv tool.',
    long_description=long_description,
    url='http://github.com/solovyevn/pyvenvwrapper',
    download_url='http://pypi.python.org/pypi/pyvenvwrapper',
    project_url=['Bug Tracker, http://github.com/solovyevn/pyvenvwrapper/issues',
                 'Documentation, http://pyvenvwrapper.readthedocs.org/en/latest/'],
    author='Nikita Solovyev',
    author_email='solovyev.nik@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Unix Shell',
        'Topic :: Software Development',
        'Topic :: System',
        'Topic :: System :: Filesystems',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Shells',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: System Shells',
        'Topic :: Terminals',
        'Topic :: Utilities'
    ],
    keywords='pyvenvwrapper pyvenv venv virtualenv bash shell console project packages pip',
    packages=['pyvenvwrapper',],
    package_data={
        'pyvenvwrapper': ['pyvenvwrapper', 'pyvenvwrapper_settings'],
    },
    entry_points={
        'console_scripts': ['pyvenvwrapper = pyvenvwrapper.install:show_info', 
                            'pyvenvwrapper_enable = pyvenvwrapper.install:pyvenvwrapper_enable', 
                            'pyvenvwrapper_disable = pyvenvwrapper.install:pyvenvwrapper_disable']
    },
    include_package_data=True,
    zip_safe=False
)
