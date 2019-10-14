#!/usr/bin/env python3.7
import os
import class_objects as media
from IO.YAML.object_to_yaml import write_python_dictionary_object_to_yaml_file as dict_to_yaml
from movies.movies_gets import get_docker_media_path
from plex_linker.parser.movies import parse_all_movies_in_yaml_dictionary as parse_movies

if __name__ == "__main__":
	g = media.Globals()
	master_dictionary = media.Movies(str(os.path.abspath(get_docker_media_path(g))))
	parse_movies(g)
	dict_to_yaml(g)
	# write a cleanup method that looks at all links and if they are not in our setup they get removed