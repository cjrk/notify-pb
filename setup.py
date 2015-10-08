#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name="notify-pb",
      version="0.1.0",
      author="Christian Jurke",
      description="Broadcast a message to all your devices using pushbullet API",

      py_modules = ['notify_pb'],
      entry_points={
          'console_scripts':
            ['notify-pb = notify_pb:main']
      },
      install_requires=['setuptools', 'requests'],
      )
