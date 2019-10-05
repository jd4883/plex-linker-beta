#!/usr/bin/env python3.7
import os
import pathlib
import subprocess
from os import environ
import requests


# noinspection PyUnusedFunction,PyUnusedFunction,PyUnusedFunction
class RadarrAPI(object):
	
	def __init__(self):
		self.host_url = str(environ['RADARR_URL'])
		self.api_key = pathlib.Path('/run/secrets/radarr_api_key').read_text().replace('\n', '')
	
	def get_movie_library(self):
		return self.request_get(f"{self.host_url}/movie").json()
	
	def lookup_movie(self, query):
		return self.request_get(f"{self.host_url}/movie/lookup?term={query}").json()
	
	def request_get(self, url, data=dict()):
		return requests.get(url, headers={'X-Api-Key': self.api_key}, json=data)
	
	def request_post(self, url, data=dict()):
		return requests.post(url, headers={'X-Api-Key': self.api_key}, json=data)
	
	def request_put(self, url, data=dict()):
		return requests.put(url, headers={'X-Api-Key': self.api_key}, json=data)
	
	def request_delete(self, url, data=dict()):
		return requests.delete(url, headers={'X-Api-Key': self.api_key}, json=data)
