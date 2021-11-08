import argparse
import os
import random


if __name__ == '__main__':

  parser = argparse.ArgumentParser()
  parser.add_argument('-o', type=str)
  parser.add_argument('-json_file', type=str)
  parser.add_argument('-num_posts_to_output', type=str)

  args = parser.parse_args()
  num_posts_to_output = int(args.num_posts_to_output)
  json_file = args.json_file
  output_json = args.o

  path_to_file = os.path.split(os.path.abspath(output_json))[0]
  if (not os.path.isdir(path_to_file)):
    os.makedirs(path_to_file)

  num_lines = sum(1 for line in open(json_file, 'r'))

  assert num_posts_to_output > 0
  random_lines = random.sample(range(1, num_lines+1), num_posts_to_output)
  random_lines.sort()
  posts = []

  f = open(json_file, 'r')

  json_lines = f.readlines()
  posts = []

  print(random_lines)

  for line_number in random_lines:
    posts.append(json_lines[line_number])

  print(posts)
