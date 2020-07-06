#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

classifiers = ['Development Status :: 5 - Production/Stable',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.6',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(
    name            = 'doublehat',
    version         = '2.2.3',
    classifiers     = classifiers,
    py_modules      = [ 'doublehat' ],
    install_requires= ['rpi_ws281x >= 3.0.3']
)
