import os
from messaging import backend as backend
import plex_linker.sets as sets
import plex_linker.fetch.series as fetch_series
from plex_linker.fetch import series as fetch_series


def parse_series_genres(sonarr_series_dict, series_dict, g):
	result = series_dict['Show Genres'] = sonarr_series_dict.pop('genres', list())
	g.LOG.debug(backend.debug_message(649, g, result))
	return list(result)


def tvdb_id(sonarr_series_dict, series_dict, g):
	result = series_dict['tvdbId'] = sonarr_series_dict.pop('tvdbId', str())
	g.LOG.debug(backend.debug_message(618, g, result))
	return str(result)


def imdb_id(sonarr_series_dict, series_dict, g):
	result = series_dict['imdbId'] = sonarr_series_dict.pop('imdbId', str())
	g.LOG.debug(backend.debug_message(650, g, result))
	return str(result)


def episode_dict_from_lookup(self, g):
	query = episode_index(self, self.sonarr_series_dict) if self.sonarr_series_dict else dict()
	g.LOG.debug(backend.debug_message(626, g, query))
	return query


def root_folder(self, g):
	default_root = f"tv/staging/{self.show}"        # adjust to be an environ
	#default_root = f"{os.environ['SONARR_DEFAULT_ROOT']}/{self.show}"
	
	for item in g.sonarr_root_folders:
		item = fetch_series.show_path_string(self, str(item['path']))
		potential = fetch_series.show_path_string(self, f"{item}{self.show}/{self.season_folder}")
		if os.path.exists(potential) and os.path.isdir(potential):
			return fetch_series.show_path_string(self, f"{item}{self.show}")
	return str(default_root)


def anime_status(self, g):
	if 'Anime' in self.series_dict and self.series_dict['Anime']:
		result = bool(self.series_dict['Anime'])
	elif 'seriesType' in self.sonarr_api_query and self.sonarr_api_query['seriesType'] == 'anime':
		result = bool(True)
	else:
		result = bool(False)
	g.LOG.debug(backend.debug_message(621, g, result))
	return result


def episode_index(self, query = dict()):
	if self.sonarr_series_dict:
		for item in query:
			if ('episodeNumber' in query) \
					and (query[item]['episodeNumber'] == self.episode) \
					and (self.season == query[item]['seasonNumber']):
				query = query[item]
	return query


def episode_id(self, g):
	result = self.series_dict['Episode ID'] \
		if 'Episode ID' in self.series_dict and str(self.series_dict['Episode ID']).isdigit() \
		else sets.set_episode_id(self, g)
	g.LOG.debug(backend.debug_message(619, g, result))
	return result

# OLD METHOD:
# 		for i in query:
# 			if int(i['seasonNumber']) == int(self.series_dict['Season']):
# 				if int(i['episodeNumber']) == int(self.series_dict['Episode'][0]):
# 					return i['id']
def episode_padding(self, g):
	result = int(3) if self.anime_status else int(os.environ['EPISODE_PADDING'])
	g.LOG.debug(backend.debug_message(621, g, result))
	return result


def parse_episode_file_id_dict(self, g):
	result = g.sonarr.get_episode_file_by_episode_id(self.episode_file_id);
	g.LOG.debug(backend.debug_message(652, g, result))
	return result


def parse_episode_dict(self, g):
	result = g.sonarr.get_episode_by_episode_id(self.episode_id);
	g.LOG.debug(backend.debug_message(623, g, result))
	return result


def episode_file_id(self, g):
	result = self.series_dict['episodeFileId'] = int(self.episode_dict.pop('episodeFileId', str()))
	g.LOG.debug(backend.debug_message(653, g, result))
	return result


def episode_number(self, g):
	result = self.series_dict['Episode'] \
		if 'Episode' in self.series_dict and self.series_dict['Episode'] \
		else str(self.episode_dict.pop('episodeNumber', str()))
	g.LOG.debug(backend.debug_message(622, g, result))
	return result


def absolute_episode_number(self, g):
	result = self.series_dict['Absolute Episode'] = str(self.episode_dict.pop('absoluteEpisodeNumber', str()))
	if not result and 'Absolute Episode' in self.series_dict:
		del self.series_dict['Absolute Episode']
	g.LOG.debug(backend.debug_message(628, g, result))
	return result


def season_from_sonarr(self, g):
	result = self.series_dict['Season'] = str(self.episode_dict.pop('seasonNumber', str())).zfill(2)
	g.LOG.debug(backend.debug_message(630, g, result))
	return result


def season_folder_from_api(self, g):
	result = self.series_dict['Parsed Season Folder'] = f"Season {self.season}"
	g.LOG.debug(backend.debug_message(631, g, result))
	return result


def show_root_folder(self, g):
	result = self.series_dict['Show Root Path'] = \
		fetch_series.show_path_string(self, self.episode_dict.pop('path', fetch_series.show_path_string(
				self, root_folder(self, g))))
	path = os.path.join(fetch_series.show_path_string(self, os.environ['DOCKER_MEDIA_PATH']), result, self.season_folder)
	os.makedirs(path, exist_ok = True)
	g.LOG.debug(backend.debug_message(632, g, result))
	return result
