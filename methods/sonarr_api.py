import os
import pathlib
import re
import time

import requests

import messaging.backend
from jobs.cleanup.cleanup import cleanup_sonarr_api_query


class SonarrAPI(object):
	def __init__(self):
		self.host_url = str(os.environ['SONARR_URL'])
		self.api_key = re.sub('\n', '', pathlib.Path('/run/secrets/sonarr_api_key').read_text())
	
	def get_episodes_by_series_id(self, series_id):
		return self.request_get(f"{self.host_url}/episode?seriesId={series_id}").json()
	
	def get_episode_by_episode_id(self, episode_id):
		return self.request_get(f"{self.host_url}/episode/{episode_id}").json()
	
	def get_episode_file_by_episode_id(self, episode_id):
		return self.request_get(f"{self.host_url}/episodefile/{episode_id}").json()
	
	def get_root_folder(self):
		return self.request_get(f"{self.host_url}/rootfolder").json()
	
	def get_series(self):
		return self.request_get(f"{self.host_url}/series").json()
	
	def refresh_series(self, series_id, data = dict()):
		return self.request_post(f"{self.host_url}/command/RefreshSeries&seriesId={series_id}", data).json()
	
	def rescan_series(self, series_id, data = dict()):
		return self.request_post(f"{self.host_url}/command/RescanSeries&seriesId={series_id}", data).json()
	
	def lookup_series(self, query, g):
		try:
			payload = cleanup_sonarr_api_query(self.request_get(f"{self.host_url}/series/lookup?term={query}").json())
		except ValueError:
			return query
		if type(payload) is list:
			payload = payload[0]
		g.LOG.debug(messaging.backend.debug_message(625, g, payload))
		return payload
	
	def request_get(self, url, data = dict()):
		backoff_timer = 10
		try:
			get_request = requests.get(url, headers = { 'X-Api-Key': self.api_key }, json = data)
			return get_request
		except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError):
			time.sleep(backoff_timer)
	
	def request_post(self, url, data = dict()):
		backoff_timer = 10
		try:
			post_request = requests.post(url, headers = { 'X-Api-Key': self.api_key }, json = data)
			return post_request
		except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError):
			time.sleep(backoff_timer)