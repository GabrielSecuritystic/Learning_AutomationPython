#Import package selenium terlebih dahulu
from selenium import webdriver

import time #mengimport library waktu agar bisa menampilkan data dengan format waktu

#membuat function untuk instalasi driver
def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options) #insialisasi dari pemanggilan driver diatas yang menggunakan nama variable options
    driver.get("http://automated.pythonanywhere.com")
    return driver


#membuat function untuk membersihkan teks secara otomatis
def clean_text(text):
    """Extract only the temparature from text"""
    output = float(text.split(": ")[1]) #artinya menghilangkan karakter :(titik dua)
    return output #disini akan menampilkan angka saja,karena disitu telah disiplit dari index awal sampai tanda :(Titik dua) akana di split

#membuat function untuk menjalankan program yang telah disusun pada function sebelumnya
def main():
    driver = get_driver()
    time.sleep(2) #memberi jeda waktu untuk menampilkan data yg berupa waktu

    #mengambil data berdasarkan element dengan path yang telah ditentukan
    element = driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[2]")

    #mengembalikan/return nilai dari function clean_text
    return clean_text(element.text)

print(main()) #menampilkan data
