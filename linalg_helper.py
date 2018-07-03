import numpy as np
from random import random
from numpy import linalg as LA


def get_normalized_random_direction():
    vec = np.array([random() - 0.5, random() - 0.5, random() - 0.5])
    return (1 / LA.norm(vec)) * vec


def translate_mat(dx, dy, dz):
    mat = np.array([[1, 0, 0, dx],
                    [0, 1, 0, dy],
                    [0, 0, 1, dz],
                    [0, 0, 0, 1]])
    return mat


def rotate_mat(roll, pitch, yaw):
    return rotate_unit_mat(roll, 'x').dot(rotate_unit_mat(pitch, 'y').dot(rotate_unit_mat(yaw, 'z')))


def rotate_unit_mat(angle, axis):
    if axis == 'x':
        return np.array([[1, 0, 0, 0],
                         [0, np.cos(angle), np.sin(angle), 0],
                         [0, -np.sin(angle), np.cos(angle), 0],
                         [0, 0, 0, 1]])
    elif axis == 'y':
        return np.array([[np.cos(angle), 0, -np.sin(angle), 0],
                         [0, 1, 0, 0],
                         [np.sin(angle), 0, np.cos(angle), 0],
                         [0, 0, 0, 1]])
    elif axis == 'z':
        return np.array([[np.cos(angle), np.sin(angle), 0, 0],
                         [-np.sin(angle), np.cos(angle), 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])
