from io import TextIOWrapper
import json
import unittest
from pathlib import Path
import os, sys
from src import compile_word_counts


parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)

class PonyTest(unittest.TestCase):

    def setUp(self):
      self.ip_folder_path = os.path.join(parentdir, 'test/fixtures')
      self.word_counts = os.path.join(self.ip_folder_path, "word_counts.true.json")

    def test_0_setup(self):
      self.assertEqual(os.path.isfile(self.word_counts), True)
      print("All files exist")


    def test_1(self):
      json_file: TextIOWrapper = open(self.word_counts, 'r')
      json_output = json.load(json_file)

      in_file_path = "word_count_test.csv"
      out_file_path = "./test1_output.json"
      compile_word_counts.main(in_file=in_file_path, out_file=out_file_path)

      output_test_json_file: TextIOWrapper = open(out_file_path, 'r')
      output_test_json = json.load(output_test_json_file)

      self.assertEqual(json_output, output_test_json)

      self.close_files(json_file)
      self.close_files(output_test_json_file)

      print('Done with test {}'.format("test 1"))

    def close_files(self, test_file: TextIOWrapper):
      test_file.close()
      self.assertEqual(test_file.closed, True)

if __name__ == '__main__':
    unittest.main()
