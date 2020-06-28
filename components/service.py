#! /usr/bin/env python

import time

import cv2

from components.affine_transformation import apply_affine_transformation
from components.clone_mask import merge_mask_with_image
from components.convex_hull import find_convex_hull
from components.delaunay_triangulation import find_delauney_triangulation
from components.landmark_detection import detect_landmarks

EXPECTED_NUM_IN = 2


def do_swap(img_1, img_2):
    # print('Input files', img1_path, img2_path)
    #
    # img_1 = cv2.imread(img1_path)
    # img_2 = cv2.imread(img2_path)

    # find the facial landmarks which return the key points of the face
    # localizes and labels areas such as eyebrows and nose
    # we are using the first face found no matter what in this case, could be expanded for multiple faces here
    landmarks_1 = detect_landmarks(img_1)[0]
    landmarks_2 = detect_landmarks(img_2)[0]

    # create a convex hull around the points, this will be like a mask for transferring the points
    # essentially this circles the face, swapping a convex hull looks more natural than a bounding box
    # we need to pass both sets of landmarks here because we map the convex hull from one face to another
    hull_1, hull_2 = find_convex_hull(landmarks_1, landmarks_2, img_1, img_2)

    # divide the boundary of the face into triangular sections to morph
    delauney_1 = find_delauney_triangulation(img_1, hull_1)
    # delauney_2 = find_delauney_triangulation(img_2, hull_2)

    # warp the source triangles onto the target face
    img_1_face_to_img_2 = apply_affine_transformation(delauney_1, hull_1, hull_2, img_1, img_2)
    # img_2_face_to_img_1 = apply_affine_transformation(delauney_2, hull_2, hull_1, img_2, img_1)

    swap_1 = merge_mask_with_image(hull_2, img_1_face_to_img_2, img_2)
    # swap_2 = merge_mask_with_image(hull_1, img_2_face_to_img_1, img_1)

    file_name = 'res/' + time.time().__str__() + '.jpg'
    cv2.imwrite(file_name, swap_1)
    return file_name
