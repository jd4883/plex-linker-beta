#!/usr/bin/env python3
from os import readlink

from jobs.set_path_permissions import (set_permissions)
from jobs.symlinking import (symlink_force)
from messaging.frontend import (method_launch,
                                method_exit)
from movies.movie.movie_gets import (get_relative_movie_path,
                                     get_movie_path)
from movies.movie.shows.show.create_class_object import create_tv_show_class_object
from movies.movie.shows.show.show_validation import (validate_ready_to_link_movie_to_show)
from movies.movie.shows.shows_validation import check_if_valid_symlink_destination, check_if_valid_symlink_target


def parse_show_to_link(show,
                       g):
	method_launch(g)
	for _ in g.movies_dictionary_object[show.movie_title]['Shows'].items():
		if validate_ready_to_link_movie_to_show(show.quality,
		                                        g):
			symlink_force(show,
			              g)
			show.absolute_movie_path = g.movies_dictionary_object[show.movie_title]['Absolute Movie Path'] = \
				str(get_movie_path(show,
				                   g))
			show.relative_movie_path = g.movies_dictionary_object[show.movie_title]['Relative Movie Path'] = \
				str(get_relative_movie_path(show,
				                            g))
			set_permissions(show,
			                g)
	method_exit(g)


def parse_shows_dictionary_object(movie_class_object,
                                  g):
	method_launch(g)
	for show in g.movies_dictionary_object[movie_class_object.movie_title]['Shows'].keys():
		relative_show_path = str(
			g.movies_dictionary_object[movie_class_object.movie_title]['Shows'][show]['Relative Show File Path'])
		absolute_movie_path = str(g.movies_dictionary_object[movie_class_object.movie_title]["Parsed Movie File"])
		try:
			if validate_strings_match(f'{relative_show_path} -> {readlink(relative_show_path)}', \
			                       g.movies_dictionary_object[movie_class_object.movie_title]['Shows'][show]['Symlinked']):
				if get_live_link(relative_show_path) and \
						(check_if_valid_symlink_destination(relative_show_path) and
						 (check_if_valid_symlink_target(absolute_movie_path))):
					print(f"No action required for {movie_class_object.movie_title}")  # make an official message handler here
					g.list_of_linked_movies.append(movie_class_object.movie_title)
					continue
		except FileNotFoundError:
			print(f'Checking for presence of "{movie_class_object.movie_title}"')
			tv_show = create_tv_show_class_object(movie_class_object,
			                                      show,
			                                      g)
			tv_show.show = show
			parse_show_to_link(tv_show,
			                   g)
		finally:
			method_exit(g)


def validate_strings_match(string1,
                           string2):
	if string1 == string2:
		return True
	return False


def get_live_link(relative_show_path):
	# probably can make the logic a bit more clever here and check if the path put together from the parsed elements
	# already has a valid link, if not parse else continue to next item
	try:
		readlink(relative_show_path)
	except FileNotFoundError:
		return False
	return True
