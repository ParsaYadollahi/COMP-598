import argparse
from io import TextIOWrapper
import json
from os import remove
import dateparser as dp
from datetime import datetime
import pytz
import dateutil.parser


input_file, output_file = None, None

def clean() -> None:
  json_file: TextIOWrapper = open(input_file, 'r')
  json_list_string: list[str] = json_file.read().split('\n')

  # 5 Remove all Malformed JSON
  for x in json_list_string:
      if len(x) == 0 or x[0] != '{' or x[-1] != '}':
        json_list_string.remove(x)

  json_list: list[str] = [json.loads(x) for x in json_list_string]

  # 1 Remove all non title and title_text
  for x in json_list:
    if 'title' not in x and 'title_text' not in x:
      json_list.remove(x)

  # 2 Rename all title_text to title
  for idx, x in enumerate(json_list):
    if 'title_text' in x:
      title = x.pop('title_text')
      k = {'title': title}
      k.update(x)
      json_list[idx] = k


  # 3 - 4 standardize times
  for x in json_list:
    if dp.parse(x['createdAt']) is None:
      json_list.remove(x)
    else:
      x['createdAt'] = pytz.UTC.normalize(dateutil.parser.parse(x['createdAt']))

  # 6 remove all post with invalid authors
  for x in json_list:
    if 'author' in x and (x['author'] == "N/A" or x['author'] == None):
      json_list.remove(x)


  # 7- 8 total count clean
  for x in json_list:
    if 'total_count' not in x or type(x['total_count']) == int:
      continue
    if type(x['total_count']) != int and type(x['total_count']) != float and type(x['total_count']) != str:
      json_list.remove(x)

    if type(x['total_count']) == float:
      x['total_count'] = int(x['total_count'])
      continue

    if (x['total_count'].startswith('-') and x['total_count'][1:].isdigit()) or x['total_count'].isdigit():
      x['total_count'] = int(x['total_count'])
    else:
      json_list.remove(x)

  # 9 tags
  for x in json_list:
    if 'tags' not in x:
      continue
    # temp tag
    new_tags = []
    for tag in x['tags']:
      if ' ' not in tag:
        new_tags.append(tag)
      else:
        new_tags.extend(tag.split())
    # replace the current tags
    x['tags'] = new_tags

  with open(output_file, "w") as f:
    f.write(json.dumps(json_list, indent=2, default=str))
  f.close()


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', type=str, required=False)
  parser.add_argument('-o', type=str, required=False)
  args = parser.parse_args()

  input_file = args.i
  output_file = args.o

  clean()
