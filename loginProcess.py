#import package selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#membuat function untuk instalasi driver

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver =webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver

#membuat function untuk menjalankan program yg sudah di inisialisasi pada function sebelumnya

def main():
    driver = get_driver()
    driver.find_element(by="id",value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id",value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(by="xpath",value="/html/body/nav/div/a").click()
    print(driver.current_url) #ini digunakan untuk mengakses halaman yg sedang diakses(saat ini)
print(main())