import argparse

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-c', type=str, required=False)
  parser.add_argument('-o', type=str, required=False)
  args = parser.parse_args()
  config_file = args.c
  output_file = args.o
