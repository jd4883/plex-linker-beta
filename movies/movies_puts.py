#!/usr/bin/env python3
from os import makedirs

from IO.YAML.yaml_to_object import *
from messaging.frontend import (method_launch,
                                method_exit)


def set_working_directory_to_media_path(media_directory):
	chdir(media_directory)


def set_working_directory_to_script_path():
	chdir(get_script_path())


def create_directory_if_not_present(path,
                                    g):
	method_launch(g)
	try:
		makedirs(path)
	except FileExistsError:
		pass
	method_exit(g)


def get_script_path():
	from IO.YAML.yaml_to_object import get_variable_from_yaml
	return get_variable_from_yaml("Script Path")


def set_nested_dictionary_key_value_pair(g,
                                         dictionary_position_key,
                                         value=str()):
	method_launch(g)
	# this helper method takes in a key and the default desired value. It then checks if the key is defined,
	# and if not it creates the key and assigns the default value. It returns the value as the data type that was fed in
	# it is good best practice to type the variables passed to this function to ensure everything is parsed properly
	try:
		if not dictionary_position_key:
			dictionary_position_key = value
	except KeyError:
		dictionary_position_key = value
	finally:
		method_exit(g)
		return dictionary_position_key
