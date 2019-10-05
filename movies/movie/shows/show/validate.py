import os


def link_ready(quality):
	if quality:
		return True
	return False


def compare_symlink_to_relpath(show):
	try:
		comparison = f"{show.relative_show_path} -> {os.readlink(show.relative_show_path)}"
	except AttributeError:
		return False
	if str(comparison) == str(show.show_dictionary["Symlinked"]):
		return True
	return False
