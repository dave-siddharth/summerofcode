import os
import math


def area(length, width):
    return length * width

def perimeter(length, width):
    return 2 * (length + width)

def volume(length, width, height):
    return length * width * height 

def surfaceArea(length, width, height):
    return 2 * (length * width + length * height + width * height)

print(area (14, 2))
print(perimeter (10, 4))
print(volume (10, 5, 3))
print(surfaceArea (10, 10, 10))