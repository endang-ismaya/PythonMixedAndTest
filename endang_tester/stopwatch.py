"""
property of: https://gist.github.com/igniteflow/1253276#file-stopwatch-py
modified by Endang
"""

import datetime


class Timer(object):
	"""A simple timer class"""

	def __init__(self):
		pass

	def start(self):
		"""Starts the timer"""
		print('-' * 50)
		self.start = datetime.datetime.now()
		return 'Start: ' + str(self.start)

	def stop(self, message="Total elapsed: "):
		"""Stops the timer.  Returns the time elapsed"""
		print()
		print('-' * 50)
		self.stop = datetime.datetime.now()
		return message + str(self.stop - self.start)

	def now(self, message="Now: "):
		"""Returns the current time with a message"""
		return message + ": " + str(datetime.datetime.now())

	def elapsed(self, message="Elapsed: "):
		"""Time elapsed since start was called"""
		return message + str(datetime.datetime.now() - self.start)

	def split(self, message="Split started at: "):
		"""Start a split timer"""
		self.split_start = datetime.datetime.now()
		return message + str(self.split_start)

	def unsplit(self, message="Unsplit: "):
		"""Stops a split. Returns the time elapsed since split was called"""
		return message + str(datetime.datetime.now() - self.split_start)
