# Latihan cara menambahkan sebuah watermark di gambar

import cv2
# load file image yg akan ditambahkan sebuah watermark
image = cv2.imread(
    'ImageProcessing/ImageProcessing/watermarking/Borobudur_Temple.jpg')
watermark = cv2.imread(
    'ImageProcessing/ImageProcessing/watermarking/watermark_indo.jpg')

print(watermark.shape)

x = image.shape[1] - watermark.shape[1]
y = image.shape[0] - watermark.shape[0]

watermark_place = image[y:, x:]

cv2.imwrite(
    'ImageProcessing/ImageProcessing/watermarking/tempat_watermark.jpg', watermark_place)
print(watermark_place.shape)

blend = cv2.addWeighted(watermark_place, 0.5, watermark, 0.5, 0)
cv2.imwrite(
    'ImageProcessing/ImageProcessing/watermarking/tempat.jpg', blend)

image[y:, x:] = blend
cv2.imwrite(
    'ImageProcessing/ImageProcessing/watermarking/elfs-watermarked.jpeg', image)
