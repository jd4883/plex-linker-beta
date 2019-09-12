#!/usr/bin/env python3
from os.path import (relpath,
                     abspath)
from os import (chdir,
                environ)

from messaging.frontend import (method_launch,
                                method_exit)


def get_media_collection_parsed_last_time():
	chdir(environ['PLEX_LINKER'])
	return "config_files/media_collection_parsed_last_run.yaml"


def get_media_collection_parsed_archives():
	chdir(environ['PLEX_LINKER'])
	return "config_files/archives"


def get_relative_movies_path(self,
                             g):
	method_launch(g)
	method_exit(g)
	return relpath(self.absolute_movies_path,
	               g.MEDIA_PATH)


def get_absolute_movies_path(g):
	method_launch(g)
	method_exit(g)
	return abspath("/".join((g.MEDIA_PATH,
	                         g.MOVIES_PATH[0])))
#
#
# def get_intersection_between_lists(a_set, b_set):
# 	return a_set & b_set
# future method for adding movies library from disk
