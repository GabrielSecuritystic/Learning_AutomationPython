#import library yang dibutuhkan

import requests
from datetime import datetime
import time

#masukan code data yang akan di scrapping
ticker = input("Enter the ticker symbol: ")

#masukan inputan data yang akan di scrapping
from_date =input("masukan data pada tanggal berapa yang akan di scrap(yyyy/mm/dd):")
to_date = input("masukan data pada tanggal berapa yang akan di scrap(yyyy/mm/dd):") #ini adalah maksimum data

from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
to_datetime = datetime.strptime(to_date, '%Y/%m/%d')

#menampilkan dari inputan data yang akan discrap(from_date and to_date)
from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))

#memasukan link url target yang akan discrap datanya kemudian disave di komputer

url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

#memasukan header information tentang web target yang akan di scrap
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

#melakukan request proses scrapping
content = requests.get(url,headers=headers).content
print(content) #mencetak hasil scrapping


#memindahkan hasil scrapping kedalam sebuah file
with open('data.txt','wb') as file:
    file.write(content)