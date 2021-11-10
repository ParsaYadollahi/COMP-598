import argparse
import requests
import json

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
