from abc import abstractproperty
import argparse
from io import TextIOWrapper
import json
import sys

def compute_title_length() -> int:
  input_file = sys.argv[1]
  title_lengths = 0
  title_counter = 0
  posts_file: TextIOWrapper = open(input_file)
  output_data = json.load(posts_file)

  for data in output_data:
    title_lengths += len(data['data']['title'])
    title_counter += 1

  return title_lengths / title_counter

if __name__ == '__main__':
  print('The average title lenght is {} words.'.format(compute_title_length()))
