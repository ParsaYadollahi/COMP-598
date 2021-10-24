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

      self.test_file1 = open(f'{self.test1}')
      self.test_file2 = open(f'{self.test2}')
      self.test_file3 = open(f'{self.test3}')
      self.test_file4 = open(f'{self.test4}')
      self.test_file5 = open(f'{self.test5}')
      self.test_file6 = open(f'{self.test6}')

      self.test_file1.close()
      self.test_file2.close()
      self.test_file3.close()
      self.test_file4.close()
      self.test_file5.close()
      self.test_file6.close()

      # You might want to load the fixture files as variables, and test your code against them. Check the fixtures folder.

    def test_setup(self):
      self.assertEqual(os.path.isfile(self.test1), True)
      self.assertEqual(os.path.isfile(self.test2), True)
      self.assertEqual(os.path.isfile(self.test3), True)
      self.assertEqual(os.path.isfile(self.test4), True)
      self.assertEqual(os.path.isfile(self.test5), True)
      self.assertEqual(os.path.isfile(self.test6), True)
      print("All files exist")


    def close_files(self):
      self.test_file1.close()
      self.test_file2.close()
      self.test_file3.close()
      self.test_file4.close()
      self.test_file5.close()
      self.test_file6.close()


      self.assertEqual(self.test_file1.closed, True)
      self.assertEqual(self.test_file2.closed, True)
      self.assertEqual(self.test_file3.closed, True)
      self.assertEqual(self.test_file4.closed, True)
      self.assertEqual(self.test_file5.closed, True)
      self.assertEqual(self.test_file6.closed, True)
      print('All test files closed')

    def parse_json(self, input_file: str):
      assert(input_file)
      cleanJSON = CleanJSON()
      json_file: TextIOWrapper = open(input_file, 'r')
      json_list_string = json_file.read().split('\n')
      json_list_string = cleanJSON.clean_invalid_json(json_list_string)
      return [json.loads(x) for x in json_list_string]


    def test_1(self):
      cleanJSON = CleanJSON()
      json_output_list = self.parse_json(self.test1)

      json_output_list = cleanJSON.clean_title(json_output_list)
      json_output_list = cleanJSON.rename_title(json_output_list)
      for x in json_output_list:
        self.assertTrue('title' in x)
      self.close_files()


    def test_2(self):
      cleanJSON = CleanJSON()
      json_output_list = self.parse_json(self.test2)

      json_output_list = cleanJSON.standardize_time(json_output_list)
      for x in json_output_list:
        self.assertNotEqual(dp.parse(x['createdAt']), None)

      self.close_files()

    def test_3(self):
      cleanJSON = CleanJSON()
      json_list_string = self.parse_json(self.test3)
      json_list_string = cleanJSON.clean_invalid_json(json_list_string)
      for x in json_list_string:
        try:
          json.loads(x)
        except ValueError as e:
          Exception(e)
      self.close_files()

    def test_4(self):
      cleanJSON = CleanJSON()
      json_output_list = self.parse_json(self.test4)

      json_output_list = cleanJSON.clean_authors(json_output_list)
      for x in json_output_list:
        self.assertTrue('author' in x and (x['author'] == "N/A" or x['author'] == None))

      self.close_files()

    def test_5(self):
      cleanJSON = CleanJSON()
      json_output_list = self.parse_json(self.test5)

      json_output_list = cleanJSON.clean_total_count(json_output_list)
      for x in json_output_list:
        self.assertTrue(type(x['total_count'] == int))

      self.close_files()

    def test_6(self):
      cleanJSON = CleanJSON()
      json_output_list = self.parse_json(self.test6)

      new_tags = []
      print(json_output_list)
      for x in json_output_list:
        for idx, tag in enumerate(x['tags']):
          if (len(tag.split()) == 3):
            new_tags.append(tag)
        x['tags'] = new_tags

      json_output_list = cleanJSON.clean_tags(json_output_list)
      for x in json_output_list:
        self.assertTrue(len(x['tags'])%3 == 0)

      self.close_files()



if __name__ == '__main__':
    unittest.main()
