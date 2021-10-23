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
  for x in json_list:
    if 'title_text' in x:
      x['title'] = x.pop('title_text')


  # 3 standardize times
  for x in json_list:
    if dp.parse(x['createdAt']) is None:
      json_list.remove(x)
    else:
      x['createdAt'] = pytz.UTC.normalize(dateutil.parser.parse(x['createdAt']))

  print()
  for el in json_list:
    print(el)








if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', type=str, required=False)
  parser.add_argument('-o', type=str, required=False)
  args = parser.parse_args()

  input_file = args.i
  output_file = args.o

  clean()
