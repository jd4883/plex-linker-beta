from methods.class_schemas import ShowLookupSchema


def init_show_object(movie, series, g):
	from methods import Show
	if not isinstance(movie.shows_dictionary[series], dict):
		return
	show = Show(g,
	            series,
	            movie.shows_dictionary[series],
	            movie.movie_dictionary)
	init_show(show, g)
	return show


def init_show(show, g):
	print("TESTING HERE")
	lookup = g.sonarr.lookup_series(show.show, g)[0]
	result = ShowLookupSchema(many = False, partial = True).load(lookup)
	print(result)
	# show.id = show.seriesId = lookup["id"]
	print(f"SERIES ID RAW: {show.id}")
	print(f"SERIES ID: {show.seriesId}")
	print(f"TITLE: {show.title}")
	show.init(g)
