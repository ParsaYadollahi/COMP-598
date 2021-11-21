import argparse
from os import name
import pandas as pd
from pandas.core.frame import DataFrame
import json
from enum import Enum
from collections import Counter


class DF(Enum):
  TITLE = 0
  NAME = 1
  DIALOGUE = 2


def main():

  parser = argparse.ArgumentParser()
  parser.add_argument('-i', help='The input file of this script.', required=True)
  parser.add_argument('-o', help='The output file of this script.', required=False)

  args = parser.parse_args()
  in_file = args.i
  out_file = args.o

  df: DataFrame = preprocess_dialogues(in_file)
  output: dict = {}

  # Do not consider "Fluttershy and other ponies"
  exclude_ponies = {'others', 'ponies', 'and', 'all'}


  p1 = 0
  p2 = 1


  pony_names = df['pony'].tolist()
  most_common_ponies = [e for e, i in Counter(pony_names).most_common(101)]

  while(p2 < len(pony_names)):
    name1 = str(df.iloc[p1, DF.NAME.value])
    name2 = str(df.iloc[p2, DF.NAME.value])

    if name1 == name2:
      p1 += 1
      p2 += 1
      continue

    if any(exlude in name2 for exlude in exclude_ponies) or name2 not in most_common_ponies:
      del pony_names[p2]
      p1 += 1
      p2 += 1
      continue

    # TODO: EPISODE partition

    if name1 not in output:
      output[name1] = {}

    if name2 not in output[name1]:
      output[name1][name2] = 1
    else:
      output[name1][name2] += 1

    p1 += 1
    p2 += 1

  print(json.dumps(output, indent=4, sort_keys=True))


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
