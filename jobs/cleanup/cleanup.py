#!/usr/bin/env python3
def cleanup_sonarr_api_query(result):
	cleanup_list = ['overview',
	                'status',
	                'network',
	                'cleanTitle',
	                'useSceneNumbering',
	                'runtime',
	                'images',
	                'seasonCount',
	                'remotePoster',
	                'added',
	                'sortTitle',
	                'lastInfoSync',
	                'titleSlug',
	                'certification',
	                'profileId',
	                'tags',
	                'ratings',
	                'qualityProfileId',
	                'tvRageId',
	                'tvMazeId',
	                'firstAired',
	                'languageProfileId',
	                'seasonFolder']
	# need to make this a dynamic alternative to the ugly code here
	i = 0
	while i < len(result):
		while j < len(cleanup_list):
			result[i].pop(j)
			j += 1
		# result[i].pop('overview')
		# result[i].pop('status')
		# result[i].pop('network')
		# result[i].pop('cleanTitle')
		# result[i].pop('useSceneNumbering')
		# result[i].pop('runtime')
		# result[i].pop('images')
		# result[i].pop('seasonCount')
		# result[i].pop('remotePoster')
		# result[i].pop('added')
		# result[i].pop('sortTitle')
		# result[i].pop('lastInfoSync')
		# result[i].pop('titleSlug')
		# result[i].pop('certification')
		# result[i].pop('profileId')
		# result[i].pop('tags')
		# result[i].pop('ratings')
		# result[i].pop('qualityProfileId')
		# result[i].pop('tvRageId')
		# result[i].pop('tvMazeId')
		# result[i].pop('firstAired')
		# result[i].pop('languageProfileId')
		# result[i].pop('seasonFolder')
		i += 1


def link_properties(movie, show):
	show.show_dictionary['Symlinked'] = str()
	show.show_dictionary['Relative Show File Path'] = str()
	movie.movie_dictionary["Parsed Movie File"] = str()
