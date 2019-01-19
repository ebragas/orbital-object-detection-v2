"""Wrapper for Planet API"""

class Client(object):

    def __init__(self):
        pass

    def hello_world(self, name=None):
        """Hello World test function"""
        return 'Hello, {}!'.format(name or "World")
