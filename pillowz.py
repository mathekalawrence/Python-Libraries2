#import the pillow library
from PIL import Image, ImageFilter, ImageDraw, ImageEnhance

import os
#open an image file
image = Image.open(mypass.jpg)
print("Original Image Size:", image.size)