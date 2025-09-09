#import the pillow library
from PIL import Image, ImageFilter, ImageDraw, ImageEnhance

import os
#open an image file
image = Image.open(mypass.jpg)
print("Original Image Size:", image.size)

resized_image = image.resize((400, 600))
print("Resized Image Size:", resized_image)
resized_image.save('Resized_mypass.jpg')
#Display the image
resized_image.show()

# Flipping and rotating/ transposing/ flipping vertically
#Enhancing the contrast
