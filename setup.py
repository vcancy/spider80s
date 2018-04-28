# -*- coding:utf-8 -*-
try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup
from codecs import open
from os import path

VERSION = '0.0.3'

AUTHOR = "vcancy"

AUTHOR_EMAIL = "happiness1019@gmail.com"

URL = "https://github.com/vcancy/spider80s"

NAME = "spider80s"

DESCRIPTION = "80s电影爬虫 输出给定电影/电视剧的迅雷下载地址"

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()


KEYWORDS = "80s  spider movies"

LICENSE = "MIT"

PACKAGES = ["spider80s"]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',

    ],
    entry_points={
        'console_scripts': [
            '80s = spider80s:main',
        ],
    },
    keywords=KEYWORDS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=PACKAGES,
    install_requires=['beautifulsoup4>=4.6.0',
                      'lxml>=4.2.1',
                      'requests>=2.18.4',
                      ],
    include_package_data=True,
    zip_safe=True,
)