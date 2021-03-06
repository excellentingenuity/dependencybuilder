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
        if required_dependencies != None and required_dependencies != '':
            self.add_dependencies(required_dependencies)
        if required_dependencies_file_path != None and required_dependencies_file_path != '':
            self.add_dependencies_from_file(required_dependencies_file_path)
        return True

    def add_dependencies_from_file(self, dependencies_file):
        self.check_dependency_list_file_path(dependencies_file)

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

    def check_dependency_list_file_path(self, dependency_list_file_path):
        cwd = os.chdir
        if os.path.isfile(cwd + dependency_list_file_path):
            try:
                file_of_dependencies = open(cwd + dependency_list_file_path, 'wb')
            except:
                raise 
            self.add_dependencies(pickle.load(file_of_dependencies))