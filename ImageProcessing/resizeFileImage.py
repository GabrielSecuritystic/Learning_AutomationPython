import cv2 #memanggil package library yg dibutuhkan

#membuat function untuk melakukan kalkulasi atau menghitung sebuah ukuran yg nantinya akan digunakan untuk resize file image
def calculate_size(scale_percentage, width, height):
  new_width = int(width * scale_percentage / 100)
  new_height = int(height * scale_percentage / 100)
  print("New Dim:", new_width, new_height)
  return (new_width, new_height)


def resize(image_path, scale_percentage, resized_path):
  image = cv2.imread(image_path) #callback parameter image_path yg mana ini akan diisi sebuah value berupa path dari file yg akan diresize
  new_dim = calculate_size(scale_percentage, image.shape[1], image.shape[0])#ini akan membaca hasil render nantinya berapa ukuran yg dihasilkan hasil resize
  resized_image = cv2.resize(image, new_dim) #melakukan proses resize
  cv2.imwrite(resized_path, resized_image)#render proses resize

resize('ImageProcessing/ImageProcessing/gravitiy.jpg', 10, 'ImageProcessing/ImageProcessing/resized-galaxy.jpeg') #disini file akan diresize menjadi 10x lebih kecil karena disitu dicantumkan nilai 10 yg artinya menjadi 10x lebih kecil dari ukuran aslinya
