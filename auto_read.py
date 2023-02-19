# -*- coding: utf-8 -*-
"""
Launcher without graphics feedback
"""

import argparse
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import pytesseract

from auto_read.processing import apply_blur_filter
from auto_read.processing import apply_otsu_threshold
from auto_read.corner_detection import detect_contour
from auto_read.corner_detection import detect_corners_from_contour
from auto_read.homography import get_target_plane_points
from auto_read.homography import unwarp
from auto_read.orientation import check_angle
from auto_read.orientation import rotate


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def trash_function():
    return None

plt.show = trash_function
parser = argparse.ArgumentParser(prog = 'Auto read')
parser.add_argument("file",help="need image path")
args = parser.parse_args()

if __name__ == "__main__":
    screenshot = input("\nIs the image a screenshot ([y]/n) ? ")
    image = cv.imread(args.file)
    img = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    if screenshot  == "n" or screenshot  == "no":
        filtered_img = apply_blur_filter(img)
        threshold_img = apply_otsu_threshold(filtered_img)
        cnv, largest_contour = detect_contour(threshold_img, image.shape)
        corners = detect_corners_from_contour(cnv, largest_contour)
        target_plane_points, h, w = get_target_plane_points(corners)
        un_warped = unwarp(image, np.float32(corners), target_plane_points)
        cropped = un_warped[int(0.05*h):int(0.95*h),int(0.05*w):int(0.95*w)]
        img_filtered = apply_blur_filter(cropped, 5)
        img_tresh = apply_otsu_threshold(img_filtered)
        angle = check_angle(img_tresh)
        img = rotate(img_tresh, angle)
    print("\nThe text extracted is:\n" )
    print(pytesseract.image_to_string(image=Image.fromarray(img)))
    print("\nEnd of auto read program")