import cv2
import random
import imageio
import argparse


def generate_random_offset(size):
    _up = random.randint(0, size)
    _down = size-_up
    _left = random.randint(0, size)
    _right = size-_left

    return _up, _down, _left, _right


parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, help="a path to a file")
parser.add_argument("-s", type=int, default=150, help="additional size of the image")

args = parser.parse_args()

image_unchanged = cv2.imread(args.f, cv2.IMREAD_UNCHANGED)
frames = []

for x in range(20):
    up, down, left, right = generate_random_offset(args.s)
    image = cv2.copyMakeBorder(image_unchanged, up, down, left, right, cv2.BORDER_CONSTANT, value=[0, 0, 0, 0])
    frames.append(cv2.cvtColor(image, cv2.COLOR_BGRA2RGBA))  # change color system from bgr to rgb

imageio.mimsave("result.gif", frames, fps=60)

