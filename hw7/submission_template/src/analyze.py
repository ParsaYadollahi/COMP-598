import argparse
import pandas as pd
import json
import os
import sys

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-o', help='The output file of this script.', required=False)
  parser.add_argument('-i', help='The input file of this script.', required=True)

  args = parser.parse_args()
  in_file = args.i

  output = {}
  categories_long = ['course-related', 'food-related', 'residence-related', 'other']
  categories = ['c', 'f', 'r', 'o']

  for category in categories:
    output.setdefault(category, 0)

  if (not os.path.isfile(in_file)):
    sys.exit("TSV file does not exist try another path")

  df = pd.read_csv(in_file, sep='\t', usecols=['coding'])

  # Count categories
  for idx, row in df.iterrows():
    output[row['coding']] += 1

  # create new dict with full key names
  new_output = {}
  for idx, (k, v) in enumerate(output.items()):
    new_output[categories_long[idx]] = v

  # dump json
  if args.o is None:
    print(json.dumps(new_output, indent=0))
  else:
    with open(args.o, 'w', encoding='utf-8') as outfile:
      json.dump(new_output, outfile, indent=0)

if __name__ == '__main__':
  main()
