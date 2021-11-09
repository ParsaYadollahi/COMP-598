import argparse
import os
import random
import json
import sys

def main():
  ##### ARGPARSE ###### ??????
  # parser = argparse.ArgumentParser()
  # parser.add_argument('-o', type=str)
  # parser.add_argument('-json_file', type=str)
  # parser.add_argument('-num_posts_to_output', type=str)

  # args = parser.parse_args()
  # num_posts_to_output = int(args.num_posts_to_output)
  # json_file = args.json_file
  # output_file = args.o


  output_file = sys.argv[2]
  json_file = sys.argv[3]
  num_posts_to_output = int(sys.argv[4])

  # Check if file exists
  path_to_file = os.path.split(os.path.abspath(output_file))[0]
  if (not os.path.isdir(path_to_file)):
    os.makedirs(path_to_file)

  # Count numb lines
  num_lines = sum(1 for line in open(json_file, 'r'))
  assert num_posts_to_output > 0

  # add every line
  if num_posts_to_output >= num_lines:
    num_posts_to_output = num_lines - 1

  # Calculate unique random lines
  random_lines = random.sample(range(0, num_lines), num_posts_to_output)
  random_lines.sort()

  f = open(json_file, 'r')
  json_lines = f.readlines()

  # Add random lines to posts
  posts = []
  for line_number in random_lines:
    posts.append(json.loads(json_lines[line_number]))

  # Write data to output file
  output_file = open(output_file, 'w')
  header = 'Name\ttitle\tcoding\n'
  output_file.write(header)

  for post in posts:
    out_line = post['data']['name'] + '\t' + post['data']['title'] + '\t' + '\n'
    output_file.write(out_line)

if __name__ == '__main__':
  main()
