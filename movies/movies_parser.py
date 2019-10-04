import class_objects as media
import messaging.frontend as message
from movies.movie.shows.shows_parse import parse_shows_dictionary_object as parse_shows


def parse_all_movies_in_yaml_dictionary(g):
	message.method_launch(g)
	for movie in sorted(g.movies_dictionary_object):
		movie = str(movie).replace(":", "-")
		# g.movies_dictionary_object[movie]['Absolute Movie File Path'] = str()
		# g.movies_dictionary_object[movie]['Parsed Movie Extension'] = str()
		# g.movies_dictionary_object[movie]['Absolute Movie Path'] = str()
		# g.movies_dictionary_object[movie]['Relative Movie File Path'] = str()
		# g.movies_dictionary_object[movie]['Relative Movie Path'] = str()
		# g.movies_dictionary_object[movie]['Parsed Movie File'] = str()
		# g.movies_dictionary_object[movie]['Parsed Movie Extension'] = str()
		try:
			self = media.Movie(movie, g.movies_dictionary_object[movie], g)
			try:
				parse_shows(self, g)
			except KeyError:
				continue
		except KeyError as err:
			self.movie_dictionary['Relative Movie Path'] = str()
			continue
	message.method_exit(g)
