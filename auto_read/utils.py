# -*- coding: utf-8 -*-
"""

This module contains utils functions

"""

import cv2
import pytesseract
import numpy as np
import matplotlib.pyplot as plt

def show_boxes_from_img(img:np.ndarray):
    """Show boxes from tesseract

    Args:
        img (np.ndarray): Source, an 8-bit single-channel image.
    """
    height = img.shape[0]

    d = pytesseract.image_to_boxes(img, output_type=pytesseract.Output.DICT)
    n_boxes = len(d['char'])
    for i in range(n_boxes):
        (__,x1,y2,x2,y1) = (d['char'][i],d['left'][i],d['top'][i],d['right'][i],d['bottom'][i])
        cv2.rectangle(img, (x1,height-y1), (x2,height-y2) , (0,255,0), 2)
    plt.imshow(img, cmap='gray')
    plt.show()