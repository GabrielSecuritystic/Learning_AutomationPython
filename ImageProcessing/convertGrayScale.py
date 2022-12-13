import cv2

color = cv2.imread('ImageProcessing/ImageProcessing/gravitiy.jpg', 0)
cv2.imwrite('ImageProcessing/ImageProcessing/galaxy-gray.jpeg', color)