# -*- coding: utf-8 -*-
"""

This module contains functions to find contours of input image

"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_contour(img:np.ndarray, img_shape:tuple):
    """Finds the largest Contour in a binary image

    Args:
        img (np.ndarray): Source, an 8-bit single-channel image.
        img_shape (tuple): Shape of the new array

    Returns:
        np.ndarray: canvas, Array of zeros with img shape 
        np.ndarray: cnt, sorted contour stored as a vector of points

    """

    canvas = np.zeros(img_shape, np.uint8)
    contours, __ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cnt = sorted(contours, key=cv2.contourArea, reverse=True)[0]
    cv2.drawContours(canvas, cnt, -1, (0, 255, 255), 3)
    plt.title('Largest Contour')
    plt.imshow(canvas)
    plt.show()

    return canvas, cnt

def detect_corners_from_contour(canvas:np.ndarray, cnt:np.ndarray):
    """Detecting corner points form contours using cv2.approxPolyDP()

    Args:
        canvas (np.ndarray): Array of zeros with img shape 
        cnt (np.ndarray): cnt, sorted contour stored as a vector of points

    Returns:
        list: sorted corner position

    """

    epsilon = 0.02 * cv2.arcLength(cnt, True)
    approx_corners = cv2.approxPolyDP(cnt, epsilon, True)
    cv2.drawContours(canvas, approx_corners, -1, (255, 255, 0), 10)
    approx_corners = sorted(np.concatenate(approx_corners).tolist())

    xaxis = 0
    yaxis = 0
    for index in range(len(approx_corners)):
        xaxis = xaxis + approx_corners[index][0]
        yaxis = yaxis + approx_corners[index][1]

    center = []
    center.append(np.int0(xaxis/len(approx_corners)))
    center.append(np.int0(yaxis/len(approx_corners)))

    rew_approx_corners = np.copy(approx_corners)
    for index in range(len(approx_corners)):
        rew_approx_corners[index][0]=approx_corners[index][0]-center[0]
        rew_approx_corners[index][1]=approx_corners[index][1]-center[1]

    theta = []
    for index in range(len(rew_approx_corners)):
        theta.append([])
        theta[index].append(np.arctan2(rew_approx_corners[index][1],rew_approx_corners[index][0]))
        theta[index].append(index)

    theta.sort()

    order = []
    for index in range(len(theta)):
        order.append(theta[index][1])

    swap=order[2]
    order[2]=order[3]
    order[3]=swap
    approx_corners = [approx_corners[i] for i in order]

    plt.imshow(canvas)
    plt.title('Corner detection')
    plt.show()

    return approx_corners
