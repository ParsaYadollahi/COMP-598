from io import TextIOWrapper
import json
import unittest
from pathlib import Path
import os, sys
import dateparser as dp
from src.clean import CleanJSON
from unittest.mock import MagicMock

parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)

class CleanTest(unittest.TestCase):

    def setUp(self):
      self.ip_folder_path = os.path.join(parentdir, 'test/fixtures')
      self.test1 = os.path.join(self.ip_folder_path, "test_1.json")
      self.test2 = os.path.join(self.ip_folder_path, "test_2.json")
      self.test3 = os.path.join(self.ip_folder_path, "test_3.json")
      self.test4 = os.path.join(self.ip_folder_path, "test_4.json")
      self.test5 = os.path.join(self.ip_folder_path, "test_5.json")
      self.test6 = os.path.join(self.ip_folder_path, "test_6.json")

      # You might want to load the fixture files as variables, and test your code against them. Check the fixtures folder.

    def test_0_setup(self):
      self.assertEqual(os.path.isfile(self.test1), True)
      self.assertEqual(os.path.isfile(self.test2), True)
      self.assertEqual(os.path.isfile(self.test3), True)
      self.assertEqual(os.path.isfile(self.test4), True)
      self.assertEqual(os.path.isfile(self.test5), True)
      self.assertEqual(os.path.isfile(self.test6), True)
      print("All files exist.")


    def close_files(self, test_file: TextIOWrapper, test_file_name: str):
      test_file.close()
      self.assertEqual(test_file.closed, True)
      print('Done with test {}.'.format(test_file_name))

    def parse_json(self, json_file: TextIOWrapper):
      assert(json_file)
      cleanJSON = CleanJSON()
      json_list_string = json_file.read().split('\n')
      json_list_string = cleanJSON.clean_invalid_json(json_list_string)
      return [json.loads(x) for x in json_list_string]


    def test_1(self):
      cleanJSON = CleanJSON()
      json_file: TextIOWrapper = open(self.test1, 'r')
      json_output_list = self.parse_json(json_file)

      json_output_list = cleanJSON.clean_title(json_output_list)
      json_output_list = cleanJSON.rename_title(json_output_list)
      for x in json_output_list:
        self.assertTrue('title' in x)
      self.close_files(json_file, 'test1')


    def test_2(self):
      cleanJSON = CleanJSON()
      json_file: TextIOWrapper = open(self.test2, 'r')
      json_output_list = self.parse_json(json_file)

      json_output_list = cleanJSON.standardize_time(json_output_list)
      for x in json_output_list:
        self.assertNotEqual(dp.parse(x['createdAt']), None)

      self.close_files(json_file, 'test2')

    def test_3(self):
      cleanJSON = CleanJSON()
      json_file: TextIOWrapper = open(self.test3, 'r')
      json_list_string = self.parse_json(json_file)
      json_list_string = cleanJSON.clean_invalid_json(json_list_string)
      for x in json_list_string:
        try:
          json.loads(x)
        except ValueError as e:
          Exception(e)
      self.close_files(json_file, 'test3')

    def test_4(self):
      cleanJSON = CleanJSON()
      json_file: TextIOWrapper = open(self.test4, 'r')
      json_output_list = self.parse_json(json_file)

      json_output_list = cleanJSON.clean_authors(json_output_list)
      for x in json_output_list:
        self.assertTrue('author' in x and (x['author'] == "N/A" or x['author'] == None))

      self.close_files(json_file, 'test4')

    def test_5(self):
      cleanJSON = CleanJSON()
      json_file: TextIOWrapper = open(self.test5, 'r')
      json_output_list = self.parse_json(json_file)

      json_output_list = cleanJSON.clean_total_count(json_output_list)
      for x in json_output_list:
        self.assertTrue(type(x['total_count'] == int))

      self.close_files(json_file, 'tes5')

    def test_6(self):
      cleanJSON = CleanJSON()
      json_file: TextIOWrapper = open(self.test6, 'r')
      json_output_list = self.parse_json(json_file)

      new_tags = []
      for x in json_output_list:
        for idx, tag in enumerate(x['tags']):
          if (len(tag.split()) == 3):
            new_tags.append(tag)
        x['tags'] = new_tags

      json_output_list = cleanJSON.clean_tags(json_output_list)
      for x in json_output_list:
        self.assertTrue(len(x['tags'])%3 == 0)

      self.close_files(json_file, 'test6')



if __name__ == '__main__':
    unittest.main()
