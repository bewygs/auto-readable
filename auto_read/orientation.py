# -*- coding: utf-8 -*-
"""

This module contains functions related to the orientations of the input images

"""

import re
import numpy as np
import pytesseract
from scipy import ndimage

def check_angle(img:np.ndarray):
    """Obtain angle of rotation if the text of the image is not aligned

    Args:
        img (np.ndarray): Source, an 8-bit single-channel image.

    Returns:
        int: angle for rotation

    """
    angle=360-int(re.search('(?<=Rotate: )\d+', pytesseract.image_to_osd(img)).group(0))

    return angle

def rotate(img:np.ndarray, angle:int):
    """rotate the image with the specified angle

    Args:
        img (np.ndarray): Source, an 8-bit single-channel image.
        angle (int): angle of rotation

    Returns:
        np.ndarray: image rotated

    """
    rotated = ndimage.rotate(img, float(angle))

    return rotated