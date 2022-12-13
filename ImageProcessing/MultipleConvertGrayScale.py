import os #install package bawaan sistem operasi yg digunakan oleh seseorang yg ada di python
import cv2 #memasang pacakge dari open cv untuk render image

images = os.listdir('ImageProcessing/ImageProcessing/images') #mengambil sebuah data list gambar yg ada disebuah folder(dalam jumlah banyak)
for image in images: #melakukan looping untuk render banyak file gambar
    print(image)
    gray = cv2.imread(f'ImageProcessing/ImageProcessing/images/{image}',0) #membaca data gambar yg ada di list folder yg sebelumnya dipanggil(di folder images)
    print(gray)
    cv2.imwrite(f'ImageProcessing/ImageProcessing/grayimages/gray-{image}',gray) #render gambar yg akan diubah ke grayscale di dipindahkan ke sebuah direktori lain

