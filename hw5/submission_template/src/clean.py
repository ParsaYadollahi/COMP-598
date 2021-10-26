import argparse
from io import TextIOWrapper
import json
from os import remove
import dateparser as dp
from datetime import datetime
import pytz
import dateutil.parser


class CleanJSON():
  def __init__(self, input_file = None, output_file = None ):
    self.input_file, self.output_file = input_file, output_file


  def open_file(self):
    assert(self.input_file)
    json_file: TextIOWrapper = open(self.input_file, 'r')
    return json_file.read().split('\n')

  def write_to_file(self, json_list: list[str]):
    assert(self.output_file)
    with open(self.output_file, "w") as f:
      f.write(json.dumps(json_list, indent=2, default=str))
    f.close()

  def clean_title(self, json_list: list[str]):
    # 1 Remove all non title and title_text
    return [x for x in json_list if 'title' in x or 'title_text' in x]

  def rename_title(self, json_list: list[str]):
    # 2 Rename all title_text to title
    for idx, x in enumerate(json_list):
      if 'title_text' in x:
        title = x.pop('title_text')
        k = {'title': title}
        k.update(x)
        json_list[idx] = k
    return json_list

  def standardize_time(self, json_list: list[str]):
    # 3 - 4 standardize times
    for x in json_list.copy():
      if dp.parse(x['createdAt']) is None:
        json_list.remove(x)
      else:
        x['createdAt'] = str(pytz.UTC.normalize(dateutil.parser.parse(x['createdAt'])))
    return json_list

  def clean_authors(self, json_list: list[str]):
    # 6 remove all post with invalid authors
    return [x for x in json_list if 'author' in x and (x['author'] != "N/A" and x['author'] != None)]

  def clean_total_count(self, json_list: list[str]):
    # 7- 8 total count clean
    for x in json_list.copy():
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
    return json_list

  def clean_tags(self, json_list: list[str]):
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
    return json_list

  def clean_invalid_json(self, json_list_string: list[str]):
    # 5 Remove all Malformed JSON
    for x in json_list_string.copy():
      if(len(x) == 0 or self.is_json(x) == False):
        json_list_string.remove(x)

    return json_list_string

  def is_json(self, myjson):
    try:
      json.loads(str(myjson))
    except ValueError as e:
      return False
    return True



  def clean(self, input_file, output_file) -> None:
    self.input_file = input_file
    self.output_file = output_file
    json_list_string = self.open_file()

    json_list_string  = self.clean_invalid_json(json_list_string)

    json_list: list[str] = [json.loads(x) for x in json_list_string]

    json_list = self.clean_title(json_list)
    json_list = self.rename_title(json_list)
    json_list = self.standardize_time(json_list)
    json_list = self.clean_authors(json_list)
    json_list = self.clean_total_count(json_list)
    json_list = self.clean_tags(json_list)

    self.write_to_file(json_list)
    return json_list


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', type=str, required=False)
  parser.add_argument('-o', type=str, required=False)
  args = parser.parse_args()
  cleanJSON = CleanJSON()
  cleanJSON.clean(args.i, args.o)
