import os
import re
import subprocess

import messaging.backend as backend
import messaging.frontend as message


def symlink_force(movie, show, g):
	message.method_launch(g)
	os.chdir(str(os.environ['HOST_MEDIA_PATH']))
	process = subprocess.Popen(["ln", "-fsvr", f"{cleanString(movie.absolute_movie_file_path, movie)}",
	                            f"{cleanString(show.relative_show_file_path, movie)}"],
	                           stderr = subprocess.DEVNULL,
	                           stdout = subprocess.PIPE)
	process = re.sub("'", "", str(iter(process.communicate()).__next__())[3:-4])
	
	g.LOG.info(backend.debug_message(654, g, process))
	message.method_exit(g)

def cleanString(string, movie):
	# TODO: make a fancier method, this is really really basic
	string = string.replace('..', '.')
	string = string.replace(':', '-')
	if string.startswith("/"):
		string = string[1:]
	return string
