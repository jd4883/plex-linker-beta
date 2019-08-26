#!/usr/bin/env python3

from subprocess import (Popen,
                        DEVNULL,
                        PIPE)

from messaging.frontend import (method_exit,
                                method_launch,
                                print_linking_show_to_movie)
from movies.movies_puts import (set_working_directory_to_media_path)


def symlink_force(show_class_object):
	method_launch(show_class_object)
	# inheritence appears broken here
	if (show_class_object.absolute_movie_file_path
	    or show_class_object.relative_show_path) \
			is not (None or 'None/'
			        or show_class_object.absolute_movie_file_path.endswith('None')
			        or show_class_object.relative_show_path.endswith('None')):
		set_working_directory_to_media_path(show_class_object.MEDIA_PATH)
		# added the popen for relative symlinking because this was not working in the os symlink built in.
		# have not done any testing in Windows only on Ubuntu 18
		process = Popen(["ln",
		                 "-fsvr",
		                 f"{show_class_object.absolute_movie_file_path}",
		                 f"{show_class_object.relative_show_path}"],
		                stderr=DEVNULL,
		                stdout=PIPE)
		print_linking_show_to_movie(show_class_object,
		                            f"{process.communicate()[0].strip()}".replace('b"', '')[:-1])
	method_exit(show_class_object)

	


def get_popen_process_string(process):
	return f"{process}"

# never hits the end of here suspect something
