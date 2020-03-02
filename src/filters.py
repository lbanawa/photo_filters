import numpy as np
import cv2


def grayscale_filter(filters_input):
    """
    Apply grayscale filter to the input images if filter_type == 'gray'

    Arguments:
        filters_input{list} -- list of numpy arrays of the input images
    Returns:
        gray_output{list} -- list of modified numpy arrays after grayscale filter is applied
    """
    gray_output = [cv2.cvtColor(single_array, cv2.COLOR_BGR2GRAY) for single_array in filters_input]
    return gray_output


def sepia_filter(filters_input:list)->list:
    """
    Apply sepia filter to the input images if filter_type == 'sepia'.
        Sourced from:  https://yabirgb.com/blog/creating-a-sepia-filter-with-python/
    Arguments:
        filters_input{list} -- list of numpy arrays of the input images
    Returns:
        sepia_output{list} -- list of modified numpy arrays after sepia filter is applied
    """
    sepia_output = []
    for single_array in filters_input:
        # Apply a transformation where we multiply each pixel
        # bgr with the matrix transformation for the sepia
        lmap = np.matrix([[ 00.272, 0.534, 0.131],
                          [ 0.349, 0.686, 0.168],
                          [ 0.393, 0.769, 0.189]])
        filt = np.array([x * lmap.T for x in single_array] )
        # Check which entries have a value greather than 255 and set it to 255
        filt[np.where(filt>255)] = 255
        sepia_output.append(filt)
    return sepia_output
