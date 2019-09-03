#!/usr/bin/env python3.7
from os import chdir

from messaging.backend import debug_message


def print_movie_file_quality(movie,
                             g):
	g.LOG.debug(debug_message(804,
	                          g,
	                          movie.quality))


def print_season_parsed_value(show_object,
                              g):
	g.LOG.debug(debug_message(825,
	                          g,
	                          show_object.season))


def message_exiting_function(g):
	chdir(g.MEDIA_DIRECTORY)
	g.LOG.debug(debug_message(990,
	                          g))


def display_show_class_attributes(show_object,
                                  g):
	method_launch(g)
	print_media_path_value(g)
	print_show_path_value(show_object,
	                      g)
	print_show_title_value(show_object,
	                       g)
	method_exit(g)


def print_show_title_value(show_object,
                           g):
	g.LOG.debug(debug_message(820,
	                          g,
	                          show_object.title))


def print_show_path_value(show_object,
                          g):
	g.LOG.debug(debug_message(819,
	                          g,
	                          show_object.show_paths))


def print_media_path_value(g):
	g.LOG.debug(debug_message(818,
	                          g,
	                          g.MEDIA_PATH))


def message_no_items_found_to_parse(g):
	g.LOG.debug(debug_message(981,
	                          g,
	                          "Nothing to parse in this directory, add handling here, moving on to better things"))


def print_movie_extension_found_to_parse(movie,
                                         g):
	g.LOG.debug(debug_message(814,
	                          g,
	                          movie.extension))


def print_movie_file_found_to_parse(movie,
                                    g):
	g.LOG.debug(debug_message(812,
	                          g,
	                          movie.movie_file))


def method_launch(g):
	from logs.bin.get_parameters import (get_child_method_string,
	                                     get_parent_method_string)
	from movies.movies_puts import (set_working_directory_to_media_path,
	                                set_working_directory_to_script_path)
	set_working_directory_to_script_path()
	g.parent_method = get_parent_method_string()
	g.method = get_child_method_string()
	set_working_directory_to_media_path(g.MEDIA_PATH)
	message_entering_function(g)


def message_entering_function(g):
	g.LOG.debug(debug_message(991,
	                          g))


def print_method_shows_dictionary_value(show_object,
                                        g):
	g.LOG.debug(debug_message(808,
	                          g,
	                          show_object.shows_dictionary_object))


def message_no_duplicates_to_remove():
	# TODO: standardize method
	"Nothing to remove here detected as a duplicate")


def method_exit(g):
	from movies.movies_puts import set_working_directory_to_script_path
	set_working_directory_to_script_path()
	message_exiting_function(g)

