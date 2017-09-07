#AIOMyAnimeList

AIOMyAnimeList is an asyncio-compliant module for scraping, reading and accessing the data from [MyAnimeList](https://myanimelist.net/)

usage:
mal_acct = AIOMyAnimeList('youraccountname')
for anime is mal_acct.anime_list:
  print("{} status: {}/{} {}".format(
        anime.anime_title,
	anime.num_watched_episodes,
	anime.anime_num_episodes,
	anime.status) # each json key is available as an attribute this this way

Each anime has the following available data, straight from the JSON:
MAL Json format is as follows:
  {     'anime_airing_status': 2,
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
        'video_url': 

