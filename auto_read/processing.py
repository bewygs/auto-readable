# -*- coding: utf-8 -*-
"""

This module contains functions for processing input image

"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_blur_filter(img:np.ndarray, kernel_size=5):
    """Apply a 5x5 kernel and apply the filter to gray scale image

    Args:
        img (np.ndarray): src image
        kernel_size (int, optional): kernel size of the correlation kernel. Defaults to 5.

    Returns:
        np.ndarray: blur img

    """
    # Convert RGB to gray shade
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Kernel parameters
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size**2)
    blur_img = cv2.filter2D(gray, -1, kernel)
    plt.imshow(cv2.cvtColor(blur_img, cv2.COLOR_BGR2RGB))
    plt.title('Blur filter applied')
    plt.show()

    return blur_img

def apply_otsu_threshold(img:np.ndarray, thresh=250, maxval=255):
    """Apply OTSU threshold with tresh as threshold value and maxval as 
    maximum value to use with the THRESH_BINARY and THRESH_BINARY_INV
    thresholding types

    Args:
        img (np.ndarray): Source, an 8-bit single-channel image.
        thresh (int, optional): threshold value. Defaults to 250.
        maxval (int, optional): maximum value. Defaults to 255.

    Returns:
        np.ndarray: the computed threshold with OTSU method

    """
    __, thresh_img = cv2.threshold(img, thresh, maxval, cv2.THRESH_OTSU)
    plt.imshow(cv2.cvtColor(thresh_img, cv2.COLOR_BGR2RGB))
    plt.title('Otsu treshold applied')
    plt.show()

    return thresh_img