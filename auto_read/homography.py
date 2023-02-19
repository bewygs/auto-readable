# -*- coding: utf-8 -*-
r"""

This module contains functions that allow us to perform a homography

The planar homography relates the transformation between two planes (original and target), up to a scale factor \(s\)

$$
s\left[\begin{array}{l}
x^{\prime} \\
y^{\prime} \\
1
\end{array}\right]=\mathbf{H}\left[\begin{array}{l}
x \\
y \\
1
\end{array}\right]=\left[\begin{array}{lll}
h_{11} & h_{12} & h_{13} \\
h_{21} & h_{22} & h_{23} \\
h_{31} & h_{32} & h_{33}
\end{array}\right]\left[\begin{array}{l}
x \\
y \\
1
\end{array}\right]
$$

With \( (x^{\prime},y^{\prime}) \) points of the target plane and \( (x,y) \) points of the original plane

The homography matrix is a 3x3 matrix but with 8 DoF (degrees of freedom) as
it is estimated up to a scale. It is generally normalized with :
$$
h_{33}=1 \text { or } h_{11}^2+h_{12}^2+h_{13}^2+h_{21}^2+h_{22}^2+h_{23}^2+h_{31}^2+h_{32}^2+h_{33}^2=1
$$

"""

import cv2
import numpy as np

def get_target_plane_points(corners:list):
    """Obtain target plane points \( (x^{\prime},y^{\prime}) \), height and width

    Args:
        corners (list): sorted corner position

    Returns:
        list: target_plane_corners
        int: height
        int: width

    """
    width_1 = np.sqrt((corners[0][0] - corners[1][0]) ** 2 + (corners[0][1] - corners[1][1]) ** 2)
    width_2 = np.sqrt((corners[2][0] - corners[3][0]) ** 2 + (corners[2][1] - corners[3][1]) ** 2)
    width = max(int(width_1), int(width_2))

    height_1 = np.sqrt((corners[0][0] - corners[2][0]) ** 2 + (corners[0][1] - corners[2][1]) ** 2)
    height_2 = np.sqrt((corners[1][0] - corners[3][0]) ** 2 + (corners[1][1] - corners[3][1]) ** 2)
    height = max(int(height_1), int(height_2))

    target_plane_corners = np.float32([(0, 0), (width - 1, 0), (0, height - 1), (width - 1, height - 1)])

    return target_plane_corners, height, width

def unwarp(img:np.ndarray, srcPoints:np.ndarray, dstPoints:np.ndarray):
    """Compute homography matrix with srcPoints and dstPoints to obtain unwarped image in the target plane

    Args:
        img (np.ndarray): src image
        srcPoints (np.ndarray): Coordinates of the points in the original plane 
        dstPoints (np.ndarray): Coordinates of the points in the target plane 

    Returns:
        np.ndarray: unwarped image

    """

    h, w = img.shape[:2]
    H, _ = cv2.findHomography(srcPoints, dstPoints, method=cv2.RANSAC, ransacReprojThreshold=3.0)
    un_warped = cv2.warpPerspective(img, H, (w, h), flags=cv2.INTER_LINEAR)

    return un_warped