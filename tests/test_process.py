import unittest
import os
from process import *


class TestReadFiles(unittest.TestCase):

    # Test if input is not a string
    def test_not_string(self):
        expected_output = (False, "Input folder must be a string.")

        test_cases = [1,    #integer
                      0.02, #float
                      [0,0],# list
                     {"test":"test"}  #dictionary
                     ]

        for test in test_cases:
            self.assertEqual(read_files(test), expected_output)


    # Test if input string is not a valid path
    def test_not_valid_path(self):
        expected_output = (False, "Input a valid folder path")

        test_cases = ["test",
                 "./I/Am/Not/A/Folder/"]

        for test in test_cases:
            self.assertEqual(read_files(test), expected_output)


    # Test if input path is path to a non-image file
    # def test_not_image(self):


if __name__ == '__main__':
    unittest.main()
