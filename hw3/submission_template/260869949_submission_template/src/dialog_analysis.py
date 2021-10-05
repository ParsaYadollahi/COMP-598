import pandas as pd
import json as js
import sys
import argparse as ap
import os

pony_names = ['twilight sparkle', 'applejack', 'rarity',
            'pinkie pie', 'rainbow dash', 'fluttershy']

output_file = sys.argv[2]
input_file = sys.argv[3]

dt = pd.read_csv(input_file, delimiter=",")
dt = dt[['pony']]

counts = {name: 0 for name in pony_names}
verbosity = {name: 0 for name in pony_names}
tot_verb = 0

for pony in dt['pony']:
  if pony.lower() in pony_names:
    counts[pony.lower()] += 1
  tot_verb += 1

for pony in verbosity:
  verbosity[pony] = round(counts[pony] / tot_verb, 2)

with open(output_file, 'w', encoding='utf-8') as f:
  js.dump({'count': counts, 'verbosity': verbosity}, f, indent = 4)
