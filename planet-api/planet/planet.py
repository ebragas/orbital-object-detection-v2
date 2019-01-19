"""Wrapper for Planet API"""

import os

class Client(object):

    def __init__(self):
        self._key = os.environ['PL_API_KEY']

    def hello_world(self, name=None):
        """Hello World test function"""
        return 'Hello, {}!'.format(name or "World")
