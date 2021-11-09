import argparse
import requests
import json

## SAMPLE ##
# {"kind": "t3", "data": {"approved_at_utc": null, "subreddit": "funny", "selftext": "", "author_fullname": "t2_865x424", "saved": false, "mod_reason_title": null, "gilded": 0, "clicked": false, "title": "I see you choosing the hard way", "link_flair_richtext": [], "subreddit_name_prefixed": "r/funny", "hidden": false, "pwls": 6, "link_flair_css_class": null, "downs": 0, "thumbnail_height": 78, "top_awarded_type": null, "hide_score": true, "name": "t3_jirz0x", "quarantine": false, "link_flair_text_color": "dark", "upvote_ratio": 1.0, "author_flair_background_color": null, "subreddit_type": "public", "ups": 1, "total_awards_received": 0, "media_embed": {}, "thumbnail_width": 140, "author_flair_template_id": null, "is_original_content": false, "user_reports": [], "secure_media": {"reddit_video": {"fallback_url": "https://v.redd.it/0o0cp0yuijv51/DASH_1080.mp4?source=fallback", "height": 750, "width": 1334, "scrubber_media_url": "https://v.redd.it/0o0cp0yuijv51/DASH_96.mp4", "dash_url": "https://v.redd.it/0o0cp0yuijv51/DASHPlaylist.mpd?a=1606354241%2CNjkwMzliMjhiNWM5YjczZWU3ZDBkNTAzZjIzZmYwZjBjM2YwMWEyNDBkMjAxMTIyZDhkYzBiNGMzMDA2ZmVlOA%3D%3D&amp;v=1&amp;f=sd", "duration": 10, "hls_url": "https://v.redd.it/0o0cp0yuijv51/HLSPlaylist.m3u8?a=1606354241%2CYTliZDRkMTEzZDAzYTQ1OTRjNDRkY2QzNTA2NTc4YjM4ZTA3YTA2MzZlNmExZjU4ZDliMzU0OWM1YzI3NzNlMA%3D%3D&amp;v=1&amp;f=sd", "is_gif": false, "transcoding_status": "completed"}}, "is_reddit_media_domain": true, "is_meta": false, "category": null, "secure_media_embed": {}, "link_flair_text": null, "can_mod_post": false, "score": 1, "approved_by": null, "author_premium": false, "thumbnail": "https://b.thumbs.redditmedia.com/ALCotJyFrIi9wS5x6GuKS68AR9HlEL0rWgZwq1lZJwQ.jpg", "edited": false, "author_flair_css_class": null, "author_flair_richtext": [], "gildings": {}, "post_hint": "hosted:video", "content_categories": null, "is_self": false, "mod_note": null, "created": 1603790998.0, "link_flair_type": "text", "wls": 6, "removed_by_category": null, "banned_by": null, "author_flair_type": "text", "domain": "v.redd.it", "allow_live_comments": false, "selftext_html": null, "likes": null, "suggested_sort": null, "banned_at_utc": null, "url_overridden_by_dest": "https://v.redd.it/0o0cp0yuijv51", "view_count": null, "archived": false, "no_follow": true, "is_crosspostable": true, "pinned": false, "over_18": false, "preview": {"images": [{"source": {"url": "https://external-preview.redd.it/HzkAPzQZkuuKJQjYr6NmWT5joGlv4uaRA5QODrR5N1o.png?format=pjpg&amp;auto=webp&amp;s=2ea23efa8928e06ee7bf4cb1587ccb889dcd4537", "width": 1334, "height": 750}, "resolutions": [{"url": "https://external-preview.redd.it/HzkAPzQZkuuKJQjYr6NmWT5joGlv4uaRA5QODrR5N1o.png?width=108&amp;crop=smart&amp;format=pjpg&amp;auto=webp&amp;s=34c147ede62f43fbd8111540968669c86079d012", "width": 108, "height": 60}, {"url": "https://external-preview.redd.it/HzkAPzQZkuuKJQjYr6NmWT5joGlv4uaRA5QODrR5N1o.png?width=216&amp;crop=smart&amp;format=pjpg&amp;auto=webp&amp;s=32401a3df82da4d6e4aeb8a7ff54e4724d12b01a", "width": 216, "height": 121}, {"url": "https://external-preview.redd.it/HzkAPzQZkuuKJQjYr6NmWT5joGlv4uaRA5QODrR5N1o.png?width=320&amp;crop=smart&amp;format=pjpg&amp;auto=webp&amp;s=67014897ae05ecad8e2ffcf84fd83838ab6464db", "width": 320, "height": 179}, {"url": "https://external-preview.redd.it/HzkAPzQZkuuKJQjYr6NmWT5joGlv4uaRA5QODrR5N1o.png?width=640&amp;crop=smart&amp;format=pjpg&amp;auto=webp&amp;s=8d971a685c15b1881d836de36b50de4edbfd2c3d", "width": 640, "height": 359}, {"url": "https://external-preview.redd.it/HzkAPzQZkuuKJQjYr6NmWT5joGlv4uaRA5QODrR5N1o.png?width=960&amp;crop=smart&amp;format=pjpg&amp;auto=webp&amp;s=9d5a645033df4957f01b7424338a955f33752a07", "width": 960, "height": 539}, {"url": "https://external-preview.redd.it/HzkAPzQZkuuKJQjYr6NmWT5joGlv4uaRA5QODrR5N1o.png?width=1080&amp;crop=smart&amp;format=pjpg&amp;auto=webp&amp;s=466bdd465b9cd3c0b9f92f143c6a37ce226e4b46", "width": 1080, "height": 607}], "variants": {}, "id": "I9Iw5t-yZc87ZZr4OUt22NZFpyZ-fcqvN8bXsPDrUPU"}], "enabled": false}, "all_awardings": [], "awarders": [], "media_only": false, "can_gild": true, "spoiler": false, "locked": false, "author_flair_text": null, "treatment_tags": [], "visited": false, "removed_by": null, "num_reports": null, "distinguished": null, "subreddit_id": "t5_2qh33", "mod_reason_by": null, "removal_reason": null, "link_flair_background_color": "", "id": "jirz0x", "is_robot_indexable": true, "report_reasons": null, "author": "Jan_a_gamer", "discussion_type": null, "num_comments": 0, "send_replies": true, "whitelist_status": "all_ads", "contest_mode": false, "mod_reports": [], "author_patreon_flair": false, "author_flair_text_color": null, "permalink": "/r/funny/comments/jirz0x/i_see_you_choosing_the_hard_way/", "parent_whitelist_status": "all_ads", "stickied": false, "url": "https://v.redd.it/0o0cp0yuijv51", "subreddit_subscribers": 33837625, "created_utc": 1603762198.0, "num_crossposts": 0, "media": {"reddit_video": {"fallback_url": "https://v.redd.it/0o0cp0yuijv51/DASH_1080.mp4?source=fallback", "height": 750, "width": 1334, "scrubber_media_url": "https://v.redd.it/0o0cp0yuijv51/DASH_96.mp4", "dash_url": "https://v.redd.it/0o0cp0yuijv51/DASHPlaylist.mpd?a=1606354241%2CNjkwMzliMjhiNWM5YjczZWU3ZDBkNTAzZjIzZmYwZjBjM2YwMWEyNDBkMjAxMTIyZDhkYzBiNGMzMDA2ZmVlOA%3D%3D&amp;v=1&amp;f=sd", "duration": 10, "hls_url": "https://v.redd.it/0o0cp0yuijv51/HLSPlaylist.m3u8?a=1606354241%2CYTliZDRkMTEzZDAzYTQ1OTRjNDRkY2QzNTA2NTc4YjM4ZTA3YTA2MzZlNmExZjU4ZDliMzU0OWM1YzI3NzNlMA%3D%3D&amp;v=1&amp;f=sd", "is_gif": false, "transcoding_status": "completed"}}, "is_video": true}}
# {"kind": "t3", "data": {"approved_at_utc": null, "subreddit": "funny", "selftext": "", "author_fullname": "t2_oand8", "saved": false, "mod_reason_title": null, "gilded": 0, "clicked": false, "title": "Salvatore Ganacci - Boycycle", "link_flair_richtext": [], "subreddit_name_prefixed": "r/funny", "hidden": false, "pwls": 6, "link_flair_css_class": null, "downs": 0, "thumbnail_height": 105, "top_awarded_type": null, "hide_score": true, "name": "t3_jiryuv", "quarantine": false, "link_flair_text_color": "dark", "upvote_ratio": 1.0, "author_flair_background_color": null, "subreddit_type": "public", "ups": 1, "total_awards_received": 0, "media_embed": {"content": "&lt;iframe width=\"600\" height=\"338\" src=\"https://www.youtube.com/embed/UZEFNHod_DU?feature=oembed&amp;enablejsapi=1\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen&gt;&lt;/iframe&gt;", "width": 600, "scrolling": false, "height": 338}, "thumbnail_width": 140, "author_flair_template_id": null, "is_original_content": false, "user_reports": [], "secure_media": {"type": "youtube.com", "oembed": {"provider_url": "https://www.youtube.com/", "version": "1.0", "title": "Salvatore Ganacci - Boycycle (feat. S\u00e9bastien Tellier) (Official Music Video)", "type": "video", "thumbnail_width": 480, "height": 338, "width": 600, "html": "&lt;iframe width=\"600\" height=\"338\" src=\"https://www.youtube.com/embed/UZEFNHod_DU?feature=oembed&amp;enablejsapi=1\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen&gt;&lt;/iframe&gt;", "author_name": "OWSLA", "provider_name": "YouTube", "thumbnail_url": "https://i.ytimg.com/vi/UZEFNHod_DU/hqdefault.jpg", "thumbnail_height": 360, "author_url": "https://www.youtube.com/user/OWSLAofficial"}}, "is_reddit_media_domain": false, "is_meta": false, "category": null, "secure_media_embed": {"content": "&lt;iframe width=\"600\" height=\"338\" src=\"https://www.youtube.com/embed/UZEFNHod_DU?feature=oembed&amp;enablejsapi=1\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen&gt;&lt;/iframe&gt;", "width": 600, "scrolling": false, "media_domain_url": "https://www.redditmedia.com/mediaembed/jiryuv", "height": 338}, "link_flair_text": null, "can_mod_post": false, "score": 1, "approved_by": null, "author_premium": false, "thumbnail": "https://b.thumbs.redditmedia.com/Mi4sXChMODJZT1otoYuHLjMAnzH9D4GPJc7Qvni1khs.jpg", "edited": false, "author_flair_css_class": null, "author_flair_richtext": [], "gildings": {}, "post_hint": "rich:video", "content_categories": null, "is_self": false, "mod_note": null, "created": 1603790982.0, "link_flair_type": "text", "wls": 6, "removed_by_category": null, "banned_by": null, "author_flair_type": "text", "domain": "youtube.com", "allow_live_comments": false, "selftext_html": null, "likes": null, "suggested_sort": null, "banned_at_utc": null, "url_overridden_by_dest": "https://www.youtube.com/watch?v=UZEFNHod_DU", "view_count": null, "archived": false, "no_follow": true, "is_crosspostable": true, "pinned": false, "over_18": false, "preview": {"images": [{"source": {"url": "https://external-preview.redd.it/Ktk7Z3yg1vYcqsvM6yscUWdyqK0MADmZ0tEypq4jbtY.jpg?auto=webp&amp;s=a1da343d7ded1095ad05eb527672d0a19c39e0c6", "width": 480, "height": 360}, "resolutions": [{"url": "https://external-preview.redd.it/Ktk7Z3yg1vYcqsvM6yscUWdyqK0MADmZ0tEypq4jbtY.jpg?width=108&amp;crop=smart&amp;auto=webp&amp;s=f54be058f1498156f44918d3038a20b28f9d3bea", "width": 108, "height": 81}, {"url": "https://external-preview.redd.it/Ktk7Z3yg1vYcqsvM6yscUWdyqK0MADmZ0tEypq4jbtY.jpg?width=216&amp;crop=smart&amp;auto=webp&amp;s=88229c9d4f00c54b60d550bc02a8bba378ce845a", "width": 216, "height": 162}, {"url": "https://external-preview.redd.it/Ktk7Z3yg1vYcqsvM6yscUWdyqK0MADmZ0tEypq4jbtY.jpg?width=320&amp;crop=smart&amp;auto=webp&amp;s=4323f610a4dd1ed85d61c1aaf749a45f704af39a", "width": 320, "height": 240}], "variants": {}, "id": "b1V3TpJaXLXWThMs-aaZO8hLvxab0C7k5_dZOvPMUbs"}], "enabled": false}, "all_awardings": [], "awarders": [], "media_only": false, "can_gild": true, "spoiler": false, "locked": false, "author_flair_text": null, "treatment_tags": [], "visited": false, "removed_by": null, "num_reports": null, "distinguished": null, "subreddit_id": "t5_2qh33", "mod_reason_by": null, "removal_reason": null, "link_flair_background_color": "", "id": "jiryuv", "is_robot_indexable": true, "report_reasons": null, "author": "TouchMyNoot", "discussion_type": null, "num_comments": 0, "send_replies": true, "whitelist_status": "all_ads", "contest_mode": false, "mod_reports": [], "author_patreon_flair": false, "author_flair_text_color": null, "permalink": "/r/funny/comments/jiryuv/salvatore_ganacci_boycycle/", "parent_whitelist_status": "all_ads", "stickied": false, "url": "https://www.youtube.com/watch?v=UZEFNHod_DU", "subreddit_subscribers": 33837625, "created_utc": 1603762182.0, "num_crossposts": 0, "media": {"type": "youtube.com", "oembed": {"provider_url": "https://www.youtube.com/", "version": "1.0", "title": "Salvatore Ganacci - Boycycle (feat. S\u00e9bastien Tellier) (Official Music Video)", "type": "video", "thumbnail_width": 480, "height": 338, "width": 600, "html": "&lt;iframe width=\"600\" height=\"338\" src=\"https://www.youtube.com/embed/UZEFNHod_DU?feature=oembed&amp;enablejsapi=1\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen&gt;&lt;/iframe&gt;", "author_name": "OWSLA", "provider_name": "YouTube", "thumbnail_url": "https://i.ytimg.com/vi/UZEFNHod_DU/hqdefault.jpg", "thumbnail_height": 360, "author_url": "https://www.youtube.com/user/OWSLAofficial"}}, "is_video": false}}
##

## INVOKED AS ##
# python collect_newest.py -o mcgill.json -s /r/mcgill
# python collect_newest.py -o concordia.json -s /r/concordia

def get_posts(sub_reddit_name):
    num_posts = 100
    try:
      data = requests.get(f'http://api.reddit.com{sub_reddit_name}/new?limit={num_posts}',
                          headers={'User-Agent': 'macos:requests (by /u/CoMpScIiZeZ)'})
    except requests.exceptions:
      print("Request Fails.")
      exit(0)

    posts = data.json()['data']['children']
    return posts


def write_posts_to_file(posts, filename):
    # posts is list of json
    children = []
    with open(filename, 'w', encoding='utf-8') as outfile:
      for post in posts:
        for child in post:
          children.append(child)

      # json.dump(children, outfile, ensure_ascii=False, indent=4)
      outfile.write(
        '\n'.join(json.dumps(i) for i in children))



if __name__ == '__main__':

  parser = argparse.ArgumentParser()
  parser.add_argument('-o', type=str, required=True)
  parser.add_argument('-s', type=str, required=True)
  args = parser.parse_args()
  output_file = args.o
  subreddit = args.s

  post_by_uni = []
  post_by_uni.append(get_posts(subreddit))

  write_posts_to_file(post_by_uni, "../{}".format(output_file))
