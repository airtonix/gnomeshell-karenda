#!/usr/bin/env python

from setuptools import setup, find_packages

import karenda as app

setup(name="gnomeshell-karenda",
      version=app.__version__,
      description="A gnomeshell dbus daemon that syncs your google calendars on access.",
      author="Zenobius Jiricek",
      author_email="airtonix@gmail.com",
      url='http://github.com/airtonix/gnomeshell-karenda',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'gdata',
          'pygtk',
          'iso8601',
          'python-dbus',
          'python-daemon',
      ],
      scripts=[
      'karenda/bin/gnomeshell-karenda',
      ],
      zip_safe=False,
      )
