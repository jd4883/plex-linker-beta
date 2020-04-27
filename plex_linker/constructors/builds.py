from marshmallow import INCLUDE, pprint, ValidationError

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
	lookup = g.sonarr.lookup_series(show.title, g)[0]
	print("PRINTING LOOKUP")
	print(lookup)
	print("PRINTING RESULT")
	try:
		result = ShowLookupSchema(many = False, partial = True, exclude = "overview").load(lookup, unknown = INCLUDE)
		print(result)
	except ValidationError as err:
		pprint(err.messages)
	
	# show.id = show.seriesId = lookup["id"]
	print(f"SERIES ID RAW: {show.id}")
	print(f"SERIES ID: {show.seriesId}")
	print(f"TITLE: {show.title}")
	# del lookup
	show.init(g)
