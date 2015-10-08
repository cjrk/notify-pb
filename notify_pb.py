#!/usr/bin/python
# -*- coding: utf-8 -*-

usage = """notify-pb <title> [body]
	Broadcast a message to all your devices.
	The message-body is optional
"""

import requests
from sys import exit,argv
import os

tokenfile = os.path.join(os.environ['HOME'], '.pushbullet_token')
f = open(tokenfile,'r')
access_token = f.readline().strip()
f.close()

class Pushbullet:

	def __init__(self, token):
		self.token = token

	def sendNotify(self,title,message=None):
		payload = {'type':'note', 'title':title}
		if message != None: payload['body'] = message
		requests.post('https://api.pushbullet.com/v2/pushes',
			headers={'Authorization':'Bearer '+access_token},
			data=payload)


def main():
	if len(argv) == 2:
		title = argv[1]
		message = None
	elif len(argv) == 3:
		title = argv[1]
		message = argv[2]
	else:
		print usage
		exit(1)

	pb = Pushbullet(access_token)
	pb.sendNotify(title,message)

if __name__ == '__main__':
	main()

