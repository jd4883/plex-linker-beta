import re


def build_movie_name_from_lookup(radarr_dictionary, movie_title):
	title = str(radarr_dictionary[0].pop('title', str(movie_title)))
	year = re.sub(" ()", str(), str(radarr_dictionary[0].pop('year', str())))
	return title + year


def init_show_object(movie, series, g):
	from class_objects import Show
	if not isinstance(movie.shows_dictionary[series], dict):
		return
	show = Show(g,
	            series,
	            str(movie.movie_title),
	            movie.shows_dictionary[series],
	            movie.movie_dictionary)
	return show
