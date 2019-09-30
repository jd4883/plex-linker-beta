#!/usr/bin/env python3
import os

import movies.movie.shows.show.validate
from messaging import frontend as message
from movies.movie.shows.show import (validate, show_puts as set_show)


def get_anime_status_from_api(show_lookup):
	if show_lookup['seriesType'] == 'anime':
		return True
	else:
		return False


def get_show_root_path(show_object, g):
	message.method_launch(g)
	os.chdir('/media')
	for show_path in show_object.show_paths:
		for path in os.listdir(show_path):
			show_object.path = "/".join((show_path, path, show_object.show))
			if os.path.exists(show_object.path):
				message.method_exit(g)
				return True
	message.method_exit(g)
	return False


def get_show(show_object, g):
	message.method_launch(g)
	show_object.show_paths = g.SHOWS_PATH
	set_show.set_show(show_object, g)
	message.method_exit(g)
	return show_object


def get_show_id(show, g):
	# assign at class object level and return
	message.method_launch(g)
	show_id = str()
	for index in g.shows_dictionary:
		if index['title'] == show:
			show_id = int(index['id'])
			break
	message.method_exit(g)
	return show_id


def get_tag_id(show, g, movie, tag):
	api_results = g.sonarr.get_all_tag_ids()['id']
	if not show.show_dictionary['Show Tags']:
		show.show_dictionary['Show Tags'] = list()
	if tag not in g.movies_dictionary_object[movie]['Shows'][show]['Show Tags'] and api_results[tag]:
		show.show_dictionary['Show Tags'].append(api_results[tag])
	return api_results[tag]