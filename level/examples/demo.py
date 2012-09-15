#! /usr/bin/python

# simple demo that transmits the top hacker news post over our network

import urllib2
import json
import time

def get_top():
	f_page = urllib2.urlopen("http://api.ihackernews.com/page").read()
	fj = json.loads(f_page)
	title = fj['items'][0]['title']
	score = fj['items'][0]['points']
	print title, score

if __name__ == '__main__':
	while True:
		get_top()
		time.sleep(5)