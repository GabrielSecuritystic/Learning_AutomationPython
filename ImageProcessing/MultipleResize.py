import cv2
import os


# membuat function untuk melakukan kalkulasi atau menghitung sebuah ukuran yg nantinya akan digunakan untuk resize file image
def calculate_size(scale_percentage, width, height):
    new_width = int(width * scale_percentage / 100)
    new_height = int(height * scale_percentage / 100)
    print("New Dim:", new_width, new_height)
    return (new_width, new_height)


def resize(image_path, scale_percentage, resized_path):
    # callback parameter image_path yg mana ini akan diisi sebuah value berupa path dari file yg akan diresize
    image = cv2.imread(image_path)
    # ini akan membaca hasil render nantinya berapa ukuran yg dihasilkan hasil resize
    new_dim = calculate_size(scale_percentage, image.shape[1], image.shape[0])
    resized_image = cv2.resize(image, new_dim)  # melakukan proses resize
    cv2.imwrite(resized_path, resized_image)  # render proses resize


# memanggil file yg akan di resize pada suatau direktori/folder
images = os.listdir('ImageProcessing/ImageProcessing/images')

# melakukan looping terhadap file yg akan dilakukan resize image
for image in images:
    resize(f'ImageProcessing/ImageProcessing/images/{image}', 10,
           f'ImageProcessing/ImageProcessing/resized/resize-{image}')
