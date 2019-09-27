#!/usr/bin/env python3
import os
import subprocess
import messaging.frontend as message


def symlink_force(show, g):
	message.method_launch(g)
	if (show.absolute_movie_file_path or show.relative_show_path) is not \
			(None or 'None/' or (show.absolute_movie_file_path.endswith('None') or show.relative_show_path.endswith('None'))):
		os.chdir(str(os.environ['HOST_MEDIA_PATH']))
		process = subprocess.Popen(["ln", "-fsvr", f"{show.absolute_movie_file_path}", f"{show.relative_show_path}"],
		                           stderr=subprocess.DEVNULL, stdout=subprocess.PIPE)
		show.show_dictionary['Symlinked'] = strip_quotes_from_string(f"{process.communicate()[0].strip()}").replace('b"', str())[:-1].rstrip()
		show.show_dictionary['Relative Show File Path'] = show.relative_show_path
		g.list_of_linked_movies.append(show.movie_title)
		show.show_dictionary['Relative Show File Path'] = show.relative_show_path
		show.movie_dictionary["Parsed Movie File"] = show.absolute_movie_file_path
		print(f"Created new Show Link: {show.show_dictionary['Symlinked']}")
	else:
		print(f'no link created for {show.absolute_movie_file_path}')
		show.show_dictionary['Symlinked'] = str()
		show.show_dictionary['Relative Show File Path'] = str()
		show.movie_dictionary["Parsed Movie File"] = str()
		g.list_of_movies_to_locate.append(show.movie_title)
	message.method_exit(g)


def strip_quotes_from_string(string):
	string.replace('"', '')
	return string.replace("'", "")
