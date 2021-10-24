import unittest
from pathlib import Path
import os, sys
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


    # def test_title(self):
        # Just an idea for a test; write your implementation


if __name__ == '__main__':
    unittest.main()
