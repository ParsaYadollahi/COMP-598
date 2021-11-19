import argparse
import json
import math
import os.path as osp
from collections import Counter
import re

def main(in_file, num_words):
  if not osp.isabs(in_file):
        in_file = osp.abspath(in_file)

  tfdif_ponies = {}
  ponies_json = {
        'twilight sparkle': 0,
        'applejack': 0,
        'rainbow dash': 0,
        'rarity': 0,
        'pinkie pie': 0,
        'fluttershy': 0
    }

  with open(in_file, 'r') as f:
    data = json.load(f)

    for (pony, words) in data.items():
      if pony not in ponies_json:
        continue
      tfdif_ponies[pony] = {}
      for (word, num_times_pony_uses_word) in words.items():
        tf = num_times_pony_uses_word
        idf = compute_idf(data, word)

        tfdif_ponies[pony][word] = tf * idf

  return_tfidf = {}
  for (pony, words) in tfdif_ponies.items():
    return_tfidf[pony] = [(w) for w, c in Counter(words).most_common(num_words)]

  output = json.dumps(return_tfidf, indent=4)
  output2 = re.sub(r'": \[\s+', '": [', output)
  output3 = re.sub(r'",\s+', '", ', output2)
  output4 = re.sub(r'"\s+\]', '"]', output3)
  print(output4)
  return return_tfidf

def compute_idf(data: dict, word: str):
  total_number_of_ponies = len(data.keys())
  number_of_ponies_that_use_word = 0

  for (k,v) in data.items():
    if word in v:
      number_of_ponies_that_use_word += 1

  assert number_of_ponies_that_use_word != 0
  return math.log(float(total_number_of_ponies / number_of_ponies_that_use_word))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-c', help='The input file of this script.', required=True)
  parser.add_argument('-n', help='The number of words.', required=True, type=int)

  args = parser.parse_args()
  in_file = args.c
  num_words = args.n

  main(in_file=in_file, num_words=num_words)
