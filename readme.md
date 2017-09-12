# AIOMyAnimeList

***
AIOMyAnimeList is an asyncio-compliant module for scraping, processing, and accessing the data from [MyAnimeList](https://myanimelist.net).

# Usage
``` python
mal_acct = AIOMyAnimeList('youraccountname')
for anime in mal_acct.anime_list:
    print('{} status: {}/{}  {}'.format(
          anime.anime_title,
          anime.num_watched_episodes,
          anime.anime_num_episodes,
          anime.status)
    )
```
***
Each object (Anime) contains the follow attributes (represented as JSON for ease of reading)

``` JSON
{
    anime_airing_status: 2,
    anime_end_date_string: '30-09-07',
    anime_id: 2001,
    anime_image_path: 'https://myanimelist.cdn-dena.com/r/96x136/images/anime/4/5123.jpg?s: 681e1f1607a8fc0d191befc509acf135',
    anime_licensors: None,
    anime_media_type_string: 'TV',
    anime_mpaa_rating_string: 'PG-13',
    anime_num_episodes: 27,
    anime_season: None,
    anime_start_date_string: '01-04-07',
    anime_studios: None,
    anime_title: 'Tengen Toppa Gurren Lagann',
    anime_url: '/anime/2001/Tengen_Toppa_Gurren_Lagann',
    days_string: None,
    finish_date_string: None,
    has_episode_video: False,
    has_promotion_video: True,
    has_video: True,
    is_added_to_list: False,
    is_rewatching: 0,
    num_watched_episodes: 27,
    priority_string: 'Low'
    score: 0,
    start_date_string: None,
    status: 2,
    storage_string: '',
    tags: '',
    video_url: '/anime/2001/Tengen_Toppa_Gurren_Lagann/video'
}
```

