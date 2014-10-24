#!/usr/bin/env python

from nose import *
from dependencybuilder.dependencybuilder import DependencyBuilder
from dependencybuilder.dependencybuilderexceptions import *

__author__ = 'James Johnson'
__version__= '1.0.0'

def test_init():
    test_dependencybuilder = DependencyBuilder()
    assert isinstance(test_dependencybuilder, DependencyBuilder)
