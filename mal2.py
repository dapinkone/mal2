#!/usr/bin/python3
# currently reads in a specific file, prints json.
# TODO: implement mal_update function
# TODO: implement get_anime_page_data(or similar) function to fill in alternative names, etc
# TODO: utilize(shutils?) to check file names in "my library" for anime
# TODO: related to the above, write comparison/identification function for filenames

import pprint
pp = pprint.PrettyPrinter(indent = 4)

f = open('mal.html', 'r')
file = f.read() # slurp whole file, because bad form.

import json
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
	data_listing = ''
	 
	# '<table class=\"list-table\" data-items=\"(\.+)\">' # we're looking for $1 here
	def handle_starttag(self, tag, attrs):
		if 'table' in tag:
			for attr in attrs:
				if attr[0] == 'data-items':
					for data in attr[1:]:
						self.data_listing += data
	
parser = MyHTMLParser()
parser.feed(file)
# MAL listing has been html parsed,
d = parser.data_listing
# load as json
json_data = json.loads(d)
pp.pprint(json_data)
"""
MAL Json format is as follows: 
[ {     'anime_airing_status': 2, 
        'anime_end_date_string': '22-09-09',
        'anime_id': 5525, # unique anime id, used for anime URL
        'anime_image_path': 'https://myanimelist.cdn-dena.com/r/96x136/images/anime/3/22605.jpg?s=a730b781b20acf18e8f102cb23965fe6',
        'anime_licensors': None,
        'anime_media_type_string': 'TV',
        'anime_mpaa_rating_string': 'PG-13',
        'anime_num_episodes': 25,
        'anime_season': None,
        'anime_start_date_string': '07-04-09',
        'anime_studios': None,
        'anime_title': '07-Ghost',
        'anime_url': '/anime/5525/07-Ghost',
        'days_string': 239, # how long it's been since started watching(start_date_string)
        'finish_date_string': None,
        'has_episode_video': False, 
        'has_promotion_video': True,
        'has_video': True,
        'is_added_to_list': False, # I don't know.
        'is_rewatching': 0,
        'num_watched_episodes': 2, # number of watched episodes(to be updated upon progression)
        'priority_string': 'Low',
        'score': 0, # scores are user assigned ratings from 0-10 inclusive.
        'start_date_string': '16-07-16', # date started watching
        'status': 1, # options are { 1: watching, 2: completed, 3: on-hold, 4: dropped, 6: plan-to-watch }
        'storage_string': '',
        'tags': '',
        'video_url': '/anime/5525/07-Ghost/video'},
	... ]
"""
