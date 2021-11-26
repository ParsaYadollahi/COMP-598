import argparse
import pandas as pd
from pandas.core.frame import DataFrame
import json
from enum import Enum
from collections import Counter


class DF(Enum):
  TITLE = 0
  NAME = 1
  DIALOGUE = 2

exclude_ponies: set[str] = {'others', 'ponies', 'and', 'all'}

'''
  python build_interaction_network.py -i /path/to/<script_input.csv> -o /path/to/<interaction_network.json>
'''
def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', help='The input file of this script.', required=True)
  parser.add_argument('-o', help='The output file of this script.', required=False)

  args = parser.parse_args()
  in_file = args.i
  out_file = args.o

  df: DataFrame = preprocess_dialogues(in_file)
  pony_names: list[str] = df['pony'].tolist()
  output: dict = {}
  p1: int = 0
  p2: int = 1

  # Sample 101 most commmon ponies EXCLUDING those with "all", "and", ...
  most_common_ponies_101 = pony_names.copy()
  for name in pony_names.copy():
    if (exclude_pony(name)):
      most_common_ponies_101.remove(name)

  most_common_ponies_101: list[str] = [e for e, i in Counter(most_common_ponies_101).most_common(101)]

  while(p2 < len(pony_names)):
    name1: str = pony_names[p1]
    name2: str = pony_names[p2]
    episode1: str = str(df.iloc[p1, DF.TITLE.value])
    episode2: str = str(df.iloc[p2, DF.TITLE.value])

    # 101 most frequent characters
    # Don’t include characters that contain xyz
    if(pony_names[p2] not in most_common_ponies_101):
      while(p2 < len(pony_names) and (pony_names[p2] not in most_common_ponies_101)):
        # Increment p2 till find valid pony
        p2 += 1
      p1 = p2
      p2 += 1
      continue

    # A character can’t talk to itself
    # Respect episode boundaries
    if name1 == name2 or episode1 != episode2:
      p1 += 1
      p2 += 1
      continue

    # init output dict
    if name1 not in output:
      output[name1] = {}

    # Increment interation
    if name2 not in output[name1]:
      output[name1][name2] = 1
    else:
      output[name1][name2] += 1

    p1 += 1
    p2 += 1

  with open(out_file, 'w') as output_file:
    json.dump(output, output_file, indent=4, sort_keys=True)
  output_file.close()


def exclude_pony(name: str):
  # Do not consider "Fluttershy and other ponies"
  return any(exlude in name.lower() for exlude in exclude_ponies)


def preprocess_dialogues(f):
  with open(f, 'r') as f:
    df = pd.read_csv(f)
    df = df[['title', 'pony', 'dialog']]

    df.dropna(how='any', inplace=True)

    for i in range(len(df['pony'])):
      df.iloc[i, 0] = df.iloc[i, 0].lower()
      df.iloc[i, 1] = str(df.iloc[i, 1].lower())

  f.close()
  return df

if __name__ == '__main__':
  main()
