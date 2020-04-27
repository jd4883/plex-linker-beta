#!/usr/bin/env python3
import os
import re

from messaging import backend as backend


def show_path_string(string):
	result = re.sub('//', '/', string)
	result = re.sub(str(os.environ['SONARR_ROOT_PATH_PREFIX']), str(), result)
	result = re.sub(':', str(), result)
	return result


# continue testing this seems right but may need more tweaks to properly handle everything
def fetch_link_status(self, episode_file_dict, relative_movie_file_path):
	try:
		root = str(os.environ['DOCKER_MEDIA_PATH'])
		os.chdir(root)
		result = bool()
		parsed_link = str()
		path = str(episode_file_dict.get('path', str()))
		prefix = str(os.environ['SONARR_ROOT_PATH_PREFIX'])
		link = re.sub(prefix, str(), path)
		if os.path.exists(re.sub('../', str(), str(link))):
			parsed_link = re.sub('../', str(), str(os.readlink(link)))
		if parsed_link and relative_movie_file_path == parsed_link and \
				os.path.exists(self.relative_show_file_path) and \
				os.path.islink(self.relative_show_file_path):
			result = bool(True)
		return result
	except OSError as err:
		print(err)
		print(f"RELATIVE MOVIE FILE PATH: {relative_movie_file_path}")
		return bool()


def parent_dict(g, movie_dict):
	result = movie_dict
	g.LOG.debug(backend.debug_message(627, g, result))
	return result
