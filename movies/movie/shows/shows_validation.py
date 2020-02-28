import os


def symlink_destination_exists(show):
	if os.path.exists(str(show.relative_show_file_path)):
		if os.path.islink(str(show.relative_show_file_path)):
			return True
	return False

def symlink_destination_in_dictionary(movie):
	if os.path.exists(movie.relative_movie_file_path) and os.path.isfile(movie.relative_movie_file_path):
		return True
	return False

def live_link_status(show):
	os.chdir(str(os.environ['DOCKER_MEDIA_PATH']))
	try:
		if not os.path.isdir(str(show.relative_show_file_path)) and os.readlink(str(show.relative_show_file_path)):
			return True
	except FileNotFoundError:
		pass
	except OSError:
		pass
	return False

def link_status(movie, show):
	if live_link_status(show):
		if symlink_destination_exists(show):
			if symlink_destination_in_dictionary(movie):
				return True
	return False

# def linking_can_be_skipped(show, movie):
# 	if show.series_dict:
# 		if link_status(movie, show):
# 			if plex_linker.compare.path.compare_symlink_to_relpath(show):
# 				return True
# 	return False
