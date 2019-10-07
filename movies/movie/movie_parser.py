import messaging.frontend as message


def extension_from_movie_file(movie,
                              g):
	message.method_launch(g)
	movie.quality = parse_proper(movie)
	message.print_movie_file_found_to_parse(movie, g)
	message.print_movie_extension_found_to_parse(movie, g)
	message.print_movie_file_quality(movie, g)
	message.method_exit(g)


def parse_remux_in_quality(quality, g):
	message.method_launch(g)
	if str(quality).lower() == "Remux-1080p.mkv".lower():
		quality = "Bluray-1080p Remux.mkv"
	message.method_exit(g)
	return quality


def parse_movie_file_quality(movie_file):
	return movie_file.split().pop()


def parse_proper(movie_class_object):
	movie.quality = parse_remux_in_quality(parse_movie_file_quality(movie.movie_file), g)
	if movie_class_object.quality.endswith(f"Proper.{movie_class_object.extension}"):
		movie_class_object.quality = f"{movie_class_object.movie_file.split().pop(-2)} {movie_class_object.quality}"
	return movie_class_object.quality
