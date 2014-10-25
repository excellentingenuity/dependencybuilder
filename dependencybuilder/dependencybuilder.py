#!/usr/bin/env python

from dependencybuilder.dependencybuilderexceptions import *

"""

    @example:
        dependency{
            'name':'argumentsprocessor',
            'local':false
        }
"""

class DependencyBuilder(object):

    __author__ = 'James Johnson'
    __version__ = '1.0.0'


    def __init__(self):
        pass

    def add_dependency(self, dependency):
        if self.validate_dependency_parameter(dependency) is True:
            return True
        return False

    def validate_dependency_parameter(self, dependency):
        if self.check_dependency_is_not_None_null(dependency) is False:
            raise DependencyisNullorNoneException()

        if self.check_dependency_type(dependency) is False:
            raise DependencyisNotDictionary()

        return True



    def check_dependency_is_not_None_null(self, dependency):
        """
        :param dependency:
        :return: True or False
        """
        if dependency is not None and dependency is not '':
            return True
        else:
            return False

    def check_dependency_type(self, dependency):
        if isinstance(dependency, dict) is not True:
            return False
        else:
            return True