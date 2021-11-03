import argparse
from io import TextIOWrapper
import bs4
import json
import requests
from requests.models import Response
import re


###### Sample config file ######
# {
# "cache_dir": "data/wdw_cache",
# "target_people": [ "robert-downey-jr", "justin-bieber" ]
# }
################################

class Collect_relationships():
  def __init__(self, config_file: str = '', output_file: str = '', data = None):
    self.config_file = config_file
    self.output_file = output_file
    self.data = data

  def main(self):
    self.read_target_people()

    for person in self.data['target_people']:
      base_url: str = 'https://www.whosdatedwho.com/dating/'
      page: Response = requests.get(base_url + person)
      soup: bs4.BeautifulSoup = bs4.BeautifulSoup(page.content, 'html.parser')

      print(soup.findAll('a', text = re.compile(r'[/dating/]\w'), href=True))



  def read_target_people(self) -> None:
    json_file: TextIOWrapper = open(self.config_file)
    self.data = json.load(json_file)



if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-c', type=str, required=False)
  parser.add_argument('-o', type=str, required=False)
  args = parser.parse_args()
  config_file = args.c
  output_file = args.o

  collect_rel = Collect_relationships(config_file=config_file, output_file=output_file)
  collect_rel.main()
