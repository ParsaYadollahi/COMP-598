import argparse
from io import TextIOWrapper
import pandas as pd
import json
import pathlib

def main(in_file, out_file):

  stopwords_path = str(pathlib.Path(__file__).parents[1].resolve()) + '{}'.format("/data/stopwords.txt")
  stopwords_file: TextIOWrapper = open(stopwords_path, 'r')
  stopwords = stopwords_file.read().splitlines()
  stopwords_file.close()

  ponies_set = {
        'twilight sparkle',
        'applejack',
        'rainbow dash',
        'rarity',
        'pinkie pie',
        'fluttershy'
    }

  # Remove punctuation and lower words
  df = preprocess_dialogues(in_file)
  output: dict = {}

  for word in range(len(df['pony'])):
    name = str(df.iloc[word, 0])
    dialogue = df.iloc[word, 1]

    # init keys (names) of dict
    if name not in ponies_set:
      continue
    if name not in output:
      output[name] = {}

    # Count number of words
    for word in dialogue.split():
      if word not in stopwords and word.isalpha():
        # init values (words) of dict[pony]
        if word not in output[name]:
          output[name][word] = 1
        else:
          output[name][word] += 1

  # Remove elements with less than 5 words
  for (pony, word_set) in output.copy().items():
    for (word, num_occurances) in word_set.copy().items():
      if num_occurances < 5:
        del output[pony][word]

  with open(out_file, 'w') as output_file:
    json.dump(output, output_file, indent=4, sort_keys=True)
  output_file.close()


def preprocess_dialogues(f):
  with open(f, 'r') as f:
    df = pd.read_csv(f)
    df = df[['pony', 'dialog']]

    df['dialog'] = df['dialog'].str.replace('<U+.*>', ' ', regex=True).replace('[()\[\],-.?!;:#&]', ' ', regex=True)
    df.dropna(how='any', inplace=True)

    for i in range(len(df['pony'])):
      df.iloc[i, 0] = df.iloc[i, 0].lower()
      df.iloc[i, 1] = str(df.iloc[i, 1].lower())

  f.close()
  return df


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-o', help='The output file of this script.', required=True)
  parser.add_argument('-d', help='The dialog file of this script.', required=True)

  args = parser.parse_args()
  out_file = args.o
  in_file = args.d

  main(in_file=in_file, out_file=out_file)
