"""A setuptools based setup module.

Based on:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

import versioneer

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    # project name
    name='binance-dex',
    # project version
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    # short description
    description='A python SDK for Binance DEX.',
    # readme
    long_description=long_description,
    # GitHub url
    url='https://github.com/cottonmalone/binance-dex',
    # author
    author='Cotton Malone',
    # author email.
    author_email='cotton.malone@mail.com',

    # Classifiers help users find your project by categorizing it.
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry'
        'Topic :: Office/Business :: Financial',
        'Topic :: Security :: Cryptography',

        # MIT license
        'License :: OSI Approved :: MIT License',

        # Compatible with Python 2 & 3
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],

    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    #
    # Note that this is a string of words separated by whitespace, not a list.
    keywords='cyrptocurrency binance dex sdk',

    # specify package
    packages=['binance', 'binance.api'],

    # required packages
    install_requires=[
        'requests'
    ],

    # extra required packages
    extras_require={
        'test': ['pytest', 'pytest-mock'],
    },

    # List additional URLs that are relevant to your project as a dict.
    project_urls={
        'Bug Reports': 'https://github.com/cottonmalone/binance-dex/issues',
        'Source': 'https://github.com/cottonmalone/binance-dex',
    }
)
