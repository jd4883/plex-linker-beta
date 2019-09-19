#!/usr/bin/env python3.7
from os.path import abspath

from IO.YAML.object_to_yaml import write_python_dictionary_object_to_yaml_file
from class_objects import Globals, \
	Movies
from movies.movies_parser import parse_all_movies_in_yaml_dictionary
from class_objects.radarr_api import *


if __name__ == "__main__":
	g = Globals()
	# need to work on assignments here, planning to pass the raw Movies, Movie, Shows, and Show dictionary respectfully
	# towards class objects for reference at init
	full_movie_database = Movies(abspath("/".join((str(environ['DOCKER_MEDIA_PATH']),
	                                               g.MOVIES_PATH[0]))))
	parse_all_movies_in_yaml_dictionary(g)
	write_python_dictionary_object_to_yaml_file(g)
