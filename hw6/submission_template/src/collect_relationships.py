import argparse
from io import TextIOWrapper
import bs4
import json
import requests
from requests.models import Response
import re
import hashlib
import os

class Collect_relationships():
  def __init__(self, config_file: str = '', output_file: str = '', output_json: dict = {}):
    self.config_file = config_file
    self.output_file = output_file
    self.output_json = output_json

  def main(self) -> None:
    config_file_data = self.read_config_file(self.config_file)

    for person in config_file_data['target_people']:
      url: str = 'https://www.whosdatedwho.com/dating/' + person
      page: Response = requests.get(url)
      hash: str = hashlib.sha1(url.encode('UTF-8')).hexdigest() + '.json'
      path_to_cached_file: str = "../" + config_file_data['cache_dir'] + '/{}'.format(hash)

      if (os.path.isfile(path_to_cached_file)):
        self.output_json.update(self.read_config_file(path_to_cached_file))
      else:
        if (not os.path.isdir("../" + config_file_data['cache_dir'])):
          os.makedirs("../" + config_file_data['cache_dir'])

        soup: bs4.BeautifulSoup = bs4.BeautifulSoup(page.content, 'html.parser')
        self.output_json[person] = []

        div_container = soup.find('div', class_='ff-panel clearfix')
        for href in div_container.findAll(href=True):
          if (re.match(r'^/dating/\w+', href['href'])):
            dated = href['href'].replace('/dating/', '')
            if dated != person:
              self.output_json[person].append(dated)

        with open(path_to_cached_file, 'w', encoding='utf-8') as f:
          json.dump({person: self.output_json[person]}, f, ensure_ascii=False, indent=4)
          f.close()

      with open(self.output_file, 'w', encoding='utf-8') as f:
        json.dump(self.output_json, f, ensure_ascii=False, indent=4)


  def read_config_file(self, file) -> dict:
    json_file: TextIOWrapper = open(file=file)
    return json.load(json_file)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-c', type=str, required=True)
  parser.add_argument('-o', type=str, required=True)
  args = parser.parse_args()
  config_file = args.c
  output_file = args.o

  collect_rel = Collect_relationships(config_file=config_file, output_file=output_file)
  collect_rel.main()
