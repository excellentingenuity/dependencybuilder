#!/usr/bin/env python

from nose.tools import assert_raises
from dependencybuilder.dependencybuilder import DependencyBuilder
from dependencybuilder.dependencybuilderexceptions import *

__author__ = 'James Johnson'
__version__= '1.0.0'

test_dependencey_builder = DependencyBuilder()

def test_init():
    local_dependencybuilder = DependencyBuilder()
    assert isinstance(local_dependencybuilder, DependencyBuilder)

def test_add_dependency():
    test_dependencey_builder.add_dependency({'name':'argumentsprocessor', 'local':False})
    assert test_dependencey_builder.dependency_list['argumentsprocessor'] == {'name':'argumentsprocessor', 'local':False}

def test_add_dependency_error():
    assert_raises(DependencyisNullorNoneException, test_dependencey_builder.add_dependency, '')
    assert_raises(DependencyisNullorNoneException, test_dependencey_builder.add_dependency, None)

def test_dependency_is_not_dictionary():
    assert_raises(DependencyisNotDictionary, test_dependencey_builder.add_dependency, 'Hello')

def test_add_dependencies():
    tlist = {
        'argumentsprocessor': {
        'name': 'argumentsprocessor',
        'local': False,
        },
        'nose': {
            'name': 'nose',
            'local': False,
        },
    }
    test_dependencey_builder.add_dependencies(tlist)
    assert tlist == test_dependencey_builder.dependency_list

def test_check_init_arguments():
    assert test_dependencey_builder.check_init_arguments(), True

