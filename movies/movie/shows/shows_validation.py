import os
from movies.movie.shows.show import validate as validate_show


# confirmed working
def symlink_destination_exists(show):
	if os.path.exists(str(show.show_dictionary['Relative Show File Path'])):
		if os.path.islink(str(show.show_dictionary['Relative Show File Path'])):
			return True
	return False


def symlink_destination_in_dictionary(movie):
	# this calculation should be much further up but i'll move it later
	movie.relative_movie_file_path = "/".join((movie.relative_movie_file_path, movie.movie_file))
	if os.path.exists(movie.relative_movie_file_path) and os.path.isfile(movie.relative_movie_file_path):
		return True
	return False


# confirmed working
def live_link_status(show):
	try:
		if os.readlink(str(show.show_dictionary['Relative Show File Path'])):
			return True
	except FileNotFoundError:
		pass
	return False


def link_status(movie, show):
	if live_link_status(show):
		if symlink_destination_exists(show):
			if symlink_destination_in_dictionary(movie):
				return True
	return False


def linking_can_be_skipped(show, movie):
	if show.show_dictionary:
		if link_status(movie, show):
			if validate_show.compare_symlink_to_relpath(show):
				return True
	return False
