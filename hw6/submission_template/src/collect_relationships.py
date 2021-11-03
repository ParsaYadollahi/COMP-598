import argparse
from io import TextIOWrapper
import bs4
import json
import requests
from requests.models import Response
import re
import hashlib
import os


###### Sample config file ######
# {
# "cache_dir": "data/wdw_cache",
# "target_people": [ "robert-downey-jr", "justin-bieber" ]
# }
################################

class Collect_relationships():
  def __init__(self, config_file: str = '', output_file: str = '', data = None, output_json = {}):
    self.config_file = config_file
    self.output_file = output_file
    self.data = data
    self.output_json = output_json

  def main(self):
    self.read_config_file()

    for person in self.data['target_people']:
      url: str = 'https://www.whosdatedwho.com/dating/' + person
      page: Response = requests.get(url)
      hash: str = hashlib.sha1(url.encode('UTF-8')).hexdigest() + '.html'
      path_to_cached_file = "../" + self.data['cache_dir'] + '/{}'.format(hash)

      if (os.path.isfile(path_to_cached_file)):
        break
      else:

        if (not os.path.isdir("../" + self.data['cache_dir'])):
          os.makedirs("../" + self.data['cache_dir'])

        soup: bs4.BeautifulSoup = bs4.BeautifulSoup(page.content, 'html.parser')
        self.output_json[person] = []

        div_container = soup.find('div', class_='ff-panel clearfix')
        for href in div_container.findAll(href=True):
          if (re.match(r'^/dating/\w+', href['href'])):
            dated = href['href'].replace('/dating/', '')
            if dated != person:
              self.output_json[person].append(dated)
      with open(path_to_cached_file, 'w', encoding='utf-8') as f:
        f.write(page.content.decode('utf8'))
        f.close()

      with open(self.output_file, 'w', encoding='utf-8') as f:
        json.dump(self.output_json, f, ensure_ascii=False, indent=4)


  def read_config_file(self) -> None:
    json_file: TextIOWrapper = open(self.config_file)
    self.data = json.load(json_file)




if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-c', type=str, required=True)
  parser.add_argument('-o', type=str, required=True)
  args = parser.parse_args()
  config_file = args.c
  output_file = args.o

  collect_rel = Collect_relationships(config_file=config_file, output_file=output_file)
  collect_rel.main()
