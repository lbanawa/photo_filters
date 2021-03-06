import unittest
import os
from src.process import *
import pandas as pd
import shutil
from PIL import Image
from glob import glob



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
    def test_not_image(self):
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

    # Test success case -- for multiple and single file inputs
    def test_for_success_case(self):
        if not os.path.exists('tmp'):
            os.makedirs('tmp')
        #create image file and save to created folder
        img = Image.new('RGB', (60, 30), color = 'red')
        img.save('tmp/pil_red.png')
        img.save('tmp/pil_red.jpg')
        img.save('tmp/pil_red.jpeg')
        status_multiple_files, output = read_files('tmp')
        status_single_file, output = read_files('tmp/pil_red.jpg')
        shutil.rmtree('tmp')
        self.assertTrue(status_multiple_files)  # Test directory input
        self.assertTrue(status_single_file)     # Test full file path input


class TestSaveFiles(unittest.TestCase):

    # Test if filtered_photos_to_save is not a list of arrays
    def test__invalid__filtered_photos_to_save(self):
        expected_output = (False, 'Filtered photos are in invalid format.')
        if not os.path.exists('tmp'):
            os.makedirs('tmp')
        test_cases = [1,                    # integer/ not a list
                     [],                    # empty list
                     ["dog", "cat", "bird"] # list of non-arrays
                     ]
        file_names = ['tmp/integer.txt,', 'tmp/empty_list.txt', 'non_array_list.txt']
        output = save_files(test_cases, file_names, 'tmp', 'test')
        shutil.rmtree('tmp')

        self.assertTrue(output, expected_output)

    # Test if filtered_photos_to_save and file_names are not same length
    def test_inputs_different_length(self):
        expected_output = (False, 'An unexpected error occured, image data does not match.')

        if not os.path.exists('tmp'):
            os.makedirs('tmp')

        img = Image.new('RGB', (60, 30), color = 'red')
        img.save('tmp/pil_red.png')
        img.save('tmp/pil_red.jpg')

        files = glob('tmp' + "/*")
        arrays = [cv2.imread(file) for file in files]

        file_names = ['tmp/pil_red.png']
        output = save_files(arrays, file_names, 'tmp', 'test')
        shutil.rmtree('tmp')

        self.assertTrue(output, expected_output)


class TestRunFilter(unittest.TestCase):

    def test_success(self):

        expected_output = ['tmp_out/pil_red.png',
                           'tmp_out/pil_red_sepia.png',
                           'tmp_out/pil_red_gray.png']

        folders = ["tmp_in", "tmp_out"]
        for f in folders:
            if not os.path.exists(f):
                os.makedirs(f)

        #create image file and save to created folder
        img = Image.new('RGB', (60, 30), color = 'red')
        img.save('tmp_in/pil_red.png')


        filter_types = ['gray', 'sepia']
        for f in filter_types:
            run_filter('tmp_in/', 'tmp_out/', f)

        out_files = glob('tmp_out/*')

        for f in folders:
            shutil.rmtree(f)

        self.assertTrue(out_files, expected_output)


if __name__ == '__main__':
    unittest.main()

