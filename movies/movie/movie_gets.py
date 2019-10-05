import os
import messaging.frontend as message
import movies.movie.movie_puts as sets


def get_relative_movie_path(movie, g):
	message.method_launch(g)
	relative_movie_path = str(os.path.relpath(movie.absolute_movie_path, str(os.environ['DOCKER_MEDIA_PATH'])))
	sets.absolute_movie_directory(movie, g)
	#sets.relative_movie_directory(movie, g)
	message.method_exit(g)
	return relative_movie_path


def get_absolute_movie_file_path(movie):
	return "/".join((movie.absolute_movie_path, movie.movie_file))



def get_relative_movie_file_path(movie):
	return os.path.relpath(movie.absolute_movie_path, str(os.environ['DOCKER_MEDIA_PATH']))


def movie_quality(quality):
	return str(quality)


# in theory this checks case combinations and titles correct, however, I am not seeing the desired results
def get_movie_path(movie, g):
	message.method_launch(g)
	movie.absolute_movie_path = str()
	for path in os.listdir(movie.absolute_movies_path):
		movie_string = '/'.join((movie.absolute_movies_path, path, movie.movie_title))
		# for item in g.radarr.get_movie_library():
		# 	print(f"ITEM TITLE {item['title']}")
		# 	if (str(item['title']).lower() ==
		# 	    movie.movie_title.lower()) or \
		# 			(str(item['title']).lower() ==
		# 			 ' '.join(str(movie.movie_title).split(' ')[:-1]).lower()) \
		# 			or ' '.join(str(item['title']).split(' ')[:-1]).lower() == \
		# 		' '.join(str(movie.movie_title).split(' ')[:-1]).lower():
		# 		print('we have a match')
		# 		print(f"PARSED TITLE: {item['title']} ({item['year']})")
		# 		break
		# 		# idea here is to replace the base title with whatever is in radarr and not care about the year initially
		# 		input
		# movie.movie_title = f"{k} ({k['year']})"
		
		#movie_string = movie.absolute_movie_path
		if os.path.exists(movie_string):
			movie.absolute_movie_path = movie_string
			message.method_exit(g)
			return movie.absolute_movie_path
	message.method_exit(g)
	return movie.absolute_movie_path


def movie_file(movie):
	return str(movie.movie_file)


def movie_extension(extension):
	return str(extension)
