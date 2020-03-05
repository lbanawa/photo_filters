from filters import *
from glob import glob
import cv2


def read_files(folder_path):
    """
    Read image files in a specified input folder.
    Arguments:
        folder_path{str} -- path to the folder holding the original images to be read
    Returns:
        arrays{list} -- list of images converted to numpy arrays
        files{list} -- list of file paths as strings
    """
    file_types = ["jpg", "jpeg", "png"]

    if type(folder_path) != str:
        return False, "Input folder must be a string."

     #determine if path is a folder or single image file
    if folder_path.split('.')[-1] not in file_types:
        files = glob(folder_path + "/*")
    else:
        files = [folder_path]

    if len(files) == 0:
        return False, "Input a valid folder path"

    for file in files:
        if file.split('.')[-1] not in file_types:
            return False, "Ayye! Yaar File Tis No Be An Image, Maytee!"

    arrays = [cv2.imread(file) for file in files]
    return True, [arrays, files]


def save_files(filtered_photos_to_save, file_names, output_folder):
    """
    Convert modified numpy arrays into images and save as original file name plus filter_type to a specified output folder.
    Arguments:
        filtered_photos_to_save{list} -- list of modified numpy arrays
        file_names{list} -- list of strings -- image file paths showing original image name
        output_folder{str} -- path to the folder to save the output images
    Returns:
        None -- modified images saved in designated output folder
    """
    for photo,f_name in zip(filtered_photos_to_save, file_names):
        if str(photo).split('(')[0] != '[[array':
            return False, "Filtered photos are in invalid format."
        else:
            for photo,f_name in zip(filtered_photos_to_save, file_names):
                # .format function turns input into a str and puts that str into position where the brackets are
                output_path = output_folder + f_name.split('/')[-1].replace('.','_{}.'.format(filter_type))
                cv2.imwrite(output_path, photo) 
            return True, "Filtered files saved successfully!"


def run_filter(input_folder, output_folder, filter_type):
    """
    Read files in the input_folder, run the specified filter_type on each image file and save new images to output_folder.
    Arguments:
        input_folder{str} -- path to the folder holding the input images
        ouput_folder{str} -- path to the folder to save the output images
        filter_type{str} --  filter to be run on images, 'gray' or 'sepia'
    Returns:
        None -- modified images saved in designated output folder
    """

    # read all files from our input path
    read_status, read_output = read_files(input_folder)

    if read_status:  # if we didn't hit any errors (read_files returned: True, [array,files])
        filters_input, file_names = read_output #then assign [array, files] to variables
    else: # we hit one of our errors (read_files returned: False, "some message")
        print(read_output) # print our returned message
        return None # don't run any more code from below

    # run correct filter type
    if filter_type == "gray":
        filtered_photos_to_save = grayscale_filter(filters_input)
    if filter_type == "sepia":
        filtered_photos_to_save = sepia_filter(filters_input)


    save_files(filtered_photos_to_save, file_names, output_folder)
