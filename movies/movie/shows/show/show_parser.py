#!/usr/bin/env python3
from os import environ

from messaging.frontend import (method_exit,
                                method_launch)
from movies.movie.shows.show.episode.episode_gets import (get_season_folder, get_padded_episode_number)
from movies.movies_puts import (create_directory_if_not_present,
                                set_nested_dictionary_key_value_pair)


def parse_show(show_object,
               g):
	from movies.movie.shows.show.show_puts import init_show_object
	method_launch(g)
	init_show_object(show_object)
	if not g.movies_dictionary_object[show_object.movie_title]['Shows'][show_object.show]['Anime']:
		g.movies_dictionary_object[show_object.movie_title]['Shows'][show_object.show]['Anime'] = False
	if not g.movies_dictionary_object[show_object.movie_title]['Shows'][show_object.show]['Season']:
		g.movies_dictionary_object[show_object.movie_title]['Shows'][show_object.show]['Season'] = str(0)
	g.movies_dictionary_object[show_object.movie_title]['Shows'][show_object.show]['Parsed Season Folder'] = \
		get_season_folder(show_object,
		                  g)
	show_object.episode = \
		set_nested_dictionary_key_value_pair(
			g.movies_dictionary_object[show_object.movie_title]['Shows'][show_object.show]['Episode'],
			str())
	show_object.absolute_episode = \
		set_nested_dictionary_key_value_pair(
			g.movies_dictionary_object[show_object.movie_title]['Shows'][show_object.show]['Absolute Episode'],
			str())
	method_launch(g)
	if g.movies_dictionary_object[show_object.movie_title]['Shows'][show_object.show]['Anime']:
		show_object.episode = "-".join(
			[get_padded_episode_number(e, 3) for e in show_object.episode])
		show_object.absolute_episode = "-".join(
			[get_padded_episode_number(e, 3) for e in show_object.absolute_episode])
	else:
		show_object.episode = "-".join([get_padded_episode_number(e, 2) for e in show_object.episode])
		show_object.absolute_episode = "-".join(
			[get_padded_episode_number(e, 2) for e in show_object.absolute_episode])
	method_exit(g)
	show_object.parsed_relative_title = \
		set_nested_dictionary_key_value_pair(g.movies_dictionary_object[show_object.movie_title]['Shows'][
			                                     show_object.show]['Parsed Relative Show Title'],
		                                     parse_show_title_from_show_dictionary(show_object,
		                                                                           g))
	
	method_exit(g)
	return show_object.parsed_relative_title


def parse_show_title_from_show_dictionary(self,
                                          g):
	method_launch(g)
	create_directory_if_not_present("/".join((self.path,
	                                          self.show_dictionary['Parsed Season Folder'])))
	if self.absolute_episode:
		self.parsed_title = set_nested_dictionary_key_value_pair(self.show_dictionary['Parsed Show Title'],
		                                                         f"{self.path}/{self.show_dictionary['Parsed Season Folder']}/{self.show} - S{self.show_dictionary['Season']}E{self.episode} (E{self.absolute_episode}) - {self.title}")
	else:
		self.parsed_title = set_nested_dictionary_key_value_pair(self.show_dictionary['Parsed Show Title'],
		                                                         f"{self.path}/{self.show_dictionary['Parsed Season Folder']}/{self.show} - S{self.show_dictionary['Season']}E{self.episode} - {self.title}")
	method_exit(g)
	return self.parsed_title


def get_parsed_show_title(show_object):
	return " ".join((show_object.parsed_title,
	                 show_object.quality))


def parse_root_path_string(sonarr_api_query):
	return str(sonarr_api_query['path']).replace(str(environ['SONARR_ROOT_PATH_PREFIX']), '')
