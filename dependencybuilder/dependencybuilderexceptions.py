#!/usr/bin/env python

__author__ = 'James Johnson'
__version__ = '1.0.0'

class DependencyBuilderException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)

class DependencyisNullorNoneException(DependencyBuilderException):
    def __init__(self):
        DependencyBuilderException.__init__(self, 'Passed Dependency Cannot be None or Null')

class DependencyisNotDictionary(DependencyBuilderException):
    def __init__(self):
        DependencyBuilderException.__init__(self, 'Passed Dependency Must be a Dictionary data type')