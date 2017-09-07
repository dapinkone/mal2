#!/usr/bin/python
"""
currently reads in a specific file, prints some data
TODO: implement mal_update function - to update website
TODO: implement get_anime_page_data(or similar) function to fill in
alternative names, etc
TODO: utilize(shutils?) to check file names in "my library" for anime
      (should this be in a different place/module?)
TODO: related to the above, write function to id anime by filename(see taiga)
TODO: utilize database solution to store data locally.
      MAL currently has 23587 anime, a bit above what i'd like to just handle
      in RAM, but we'll see how big that really is.
      could use mongodb for db queries; note: ea entry is ~1000 chars of json
TODO: how do I even async/threading for getting pages, or being used async
TODO: make a more complex/complete Anime type; how to handle alternative_names?
"""

import json
from html.parser import HTMLParser
import pprint
from collections import namedtuple
import asyncio

pp = pprint.PrettyPrinter(indent=4)
f = open('mal.html', 'r')
htmlfile = f.read()  # slurp whole file, because bad form.


class MyHTMLParser(HTMLParser):
    data_listing = ''
    # MADNESS
    # we're looking for $1 here? is this regex? what is this?
    # '<table class=\"list-table\" data-items=\"(\.+)\">'

    def handle_starttag(self, tag, attrs):
        if 'table' in tag:
            for attr in attrs:
                if attr[0] == 'data-items':
                    for data in attr[1:]:
                        self.data_listing += data


class AIOMyAnimeList():  # seems a good name, since we have aiohttp, etc

    def __init__(self, account):
        self._parser = MyHTMLParser()
        asyncio.sleep(0)
        self._parser.feed(htmlfile)  # TODO: get account page here for this
        asyncio.sleep(0)
        self._json_data = json.loads(self._parser.data_listing)
        # use namedtuple to build an Anime type.
        Anime = namedtuple('Anime', self._json_data[0].keys())
        self.anime_list = [Anime(**animedict) for animedict in self._json_data]


if __name__ == "__main__":
    mal_acct = AIOMyAnimeList('dapinkone')
    pp.pprint(mal_acct.anime_list)
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
