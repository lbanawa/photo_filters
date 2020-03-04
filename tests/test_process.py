import unittest
import os
from process import *
import pandas as pd
import shutil
from PIL import Image


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


    # Test if input files in valid path are not images
    def test__read_files__not_image(self):
        expected_output = (False, 'Ayye! Yaar File Tis No Be An Image, Maytee!')
    
        #make temporary folder for non-image test files
        if not os.path.exists('tmp'):
            os.makedirs('tmp')
    
        #create .txt file and save to created folder
        text_file = open("tmp/phototest.txt","w+")
        for i in range(5): 
            text_file.write("This is line %d\r\n" % (i+1))
        text_file.close()
        
        #create .csv file and save to created folder
        pd.DataFrame([1,2,3]).to_csv('tmp/testfile.csv')
        
        output = read_files('tmp')
        shutil.rmtree('tmp')
        
        self.assertEqual(output, expected_output)

    # Test success case
    def test_for_success_case(self):
    
        if not os.path.exists('tmp'):
            os.makedirs('tmp')
        
        #create image file and save to created folder
        img = Image.new('RGB', (60, 30), color = 'red')
        img.save('tmp/pil_red.png')
        img.save('tmp/pil_red.jpg')
        img.save('tmp/pil_red.jpeg')
        
        status, output = read_files('tmp')
        
        shutil.rmtree('tmp')
        
        self.assertTrue(status)
    


if __name__ == '__main__':
    unittest.main()

