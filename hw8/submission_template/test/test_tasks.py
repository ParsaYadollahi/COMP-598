from io import TextIOWrapper
import unittest
from pathlib import Path
import os, sys
import json
from src import compile_word_counts
from src import compute_pony_lang

parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)


class TasksTest(unittest.TestCase):
    def setUp(self):
      dir = os.path.dirname(__file__)
      self.mock_dialog = os.path.join(dir, 'fixtures', 'mock_dialog.csv')
      self.true_word_counts = os.path.join(dir, 'fixtures', 'word_counts.true.json')
      self.true_tf_idfs = os.path.join(dir, 'fixtures', 'tf_idfs.true.json')


    def test_task1(self):
      print(f"\nRUNNING TASK 1")
      # use  self.mock_dialog and self.true_word_counts; REMOVE self.assertTrue(True) and write your own assertion, i.e. self.assertEquals(...)
      json_file: TextIOWrapper = open(self.true_word_counts, 'r')
      json_output = json.load(json_file)


      out_file_path = './test1_output.json'
      compile_word_counts.main(in_file=self.mock_dialog, out_file=out_file_path)

      output_test_json_file: TextIOWrapper = open(out_file_path, 'r')
      output_test_json = json.load(output_test_json_file)

      self.assertEqual(json_output, output_test_json)

      self.close_files(json_file)
      self.close_files(output_test_json_file)

      print('{}'.format("test_task1 OK."))

    def test_task2(self):
      print(f"\nRUNNING TASK 2")
      # use self.true_word_counts self.true_tf_idfs; REMOVE self.assertTrue(True) and write your own assertion, i.e. self.assertEquals(...)
      # use  self.mock_dialog and self.true_word_counts; REMOVE self.assertTrue(True) and write your own assertion, i.e. self.assertEquals(...)
      json_file: TextIOWrapper = open(self.true_tf_idfs, 'r')
      json_output = json.load(json_file)

      tfidf_output = compute_pony_lang.main(in_file=self.true_word_counts, num_words=2)

      self.assertEqual(json_output, tfidf_output)
      self.close_files(json_file)

      print('{}'.format("test_task2 OK."))

    def close_files(self, test_file: TextIOWrapper):
      test_file.close()
      self.assertEqual(test_file.closed, True)


if __name__ == '__main__':
    unittest.main()
