#!/usr/bin/env python

from dependencybuilder.dependencybuilderexceptions import *
import pickle
import os
import sys


class DependencyBuilder(object):
    """

        @example:
            dependency{
                'name':'argumentsprocessor',
                'local':false
            }

            dependencies {
                dependency{
                    'name':'argumentsprocessor',
                    'local':false
                }
                dependency{
                    'name':'argumentsprocessor',
                    'local':false
                }
            }
    """
    __author__ = 'James Johnson'
    __version__ = '1.0.0'

    dependency_list = {}

    def __init__(self, required_dependencies=None, required_dependencies_file_path=None):
        self.check_init_arguments(required_dependencies, required_dependencies_file_path)

        # TODO: implement this function

    def check_init_arguments(self, required_dependencies=None, required_dependencies_file_path=None):
        pass

    def add_dependency(self, dependency):
        if self.validate_dependency_parameter(dependency) is True:
            self.dependency_list[dependency['name']] = dependency

    def add_dependencies(self, dependencies):
        for (dependency_key, dependency_value) in dependencies.items():
            self.add_dependency(dependency_value)

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
        """
        :param dependency:
        :return: True or False
        """
        if isinstance(dependency, dict) is not True:
            return False
        else:
            return True
