#!/usr/bin/env python

__author__ = 'James Johnson'
__version__ = '1.0.0'

class DependencyBuilderException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)
