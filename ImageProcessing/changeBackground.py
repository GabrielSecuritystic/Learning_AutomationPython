import cv2
import numpy as np

foreground = cv2.imread(
    'ImageProcessing/ImageProcessing/change-background/giraffe.jpeg')
background = cv2.imread(
    'ImageProcessing/ImageProcessing/change-background/safari.jpeg')

print(foreground[40, 40])
width = foreground.shape[1]
height = foreground.shape[0]
print(foreground.shape)

resized_background = cv2.resize(background, (width, height))

for i in range(width):
    for j in range(height):
        pixel = foreground[j, i]
        if np.any(pixel == [1, 255, 0]):
            foreground[j, i] = resized_background[j, i]

cv2.imwrite(
    'ImageProcessing/ImageProcessing/change-background/output.jpeg', foreground)
