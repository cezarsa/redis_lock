#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the MIT license: 
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2012 cezarsa@gmail.com

from setuptools import setup
from redis_lock import __version__

setup(
  name = 'redis-lock',
  version = __version__,
  description = "A simple pessimistic lock implementation using Redis",
  long_description = """
  A simple pessimistic lock implementation using Redis based on
  the algorithm described in http://redis.io/commands/setnx
""",
  keywords = 'redis pessimistic lock setnx',
  author = 'Cezar Sá Espinola',
  author_email = 'cezarsa@gmail.com',
  url = 'http://github.com/cezarsa/redis_lock',
  license = 'MIT',
  classifiers = ['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'Natural Language :: English',
                 'Operating System :: MacOS',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python :: 2.7'
  ],
  packages = ['redis_lock'],
  package_dir = {"redis_lock": "redis_lock"}
)

