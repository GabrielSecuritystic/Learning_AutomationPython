#memanggil library selenium
from selenium import webdriver

#set atau mengatur opsi untuk membuat browsing lebih mudah
# driver = webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe")
# driver.get("https://www.google.com/")

#membuat function di python untuk instalasi package yg dibutuhkan
def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized") #unutk meruhbah
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    #memasukan add_argument unutk ditambahkan kedalam sebuah tag yang akan dilakukan otomasi

    driver = webdriver.Chrome(options=options)
    driver.get("https://automated.pythonanywhere.com")
    return driver

#membuat function untuk menjalankan program
def main():
    driver = get_driver()
    #memanggil element yang akan ditampilkan versi 1
    # element = driver.find_element_by_xpath("/html/body/div[1]/div/h1[1]")

    #memanggil element yang akan ditampilkan versi 2
    element = driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[1]")
    return element.text

#mencetak hasil program agar tampil
print(main())