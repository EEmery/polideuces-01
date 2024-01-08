import numpy as np
from PIL import Image


def get_steer(hor):
    left = 1.0
    right = 1.0

    if hor > 0:
        right = 1 - hor
    if hor < 0:
        left = hor + 1

    return left, right


def get_power(left_steer, right_steer, acceleration, max_speed):
    left_power = left_steer * acceleration * max_speed
    right_power = right_steer * acceleration * max_speed

    return left_power, right_power


def get_acceleration(acc, rev):
    return ((acc + 1) - (rev + 1)) / 2


def format_lin_acc(lin_acc):
    xyz = [lin_acc.x, lin_acc.y, lin_acc.z]

    return [round(i, 2) for i in xyz]


def format_frame(frame, scale_factor=1):
    x, y = frame.size
    new_x = int(x * scale_factor)
    new_y = int(y * scale_factor)

    frame = frame.resize((new_x, new_y), Image.Resampling.LANCZOS)
    frame = np.array(frame)

    return frame
