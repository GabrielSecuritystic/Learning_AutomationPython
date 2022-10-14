#memanggil package beautifulsoup
from bs4 import BeautifulSoup

#install package requests
import requests

#membuat function untuk merancang program

def get_currency(in_currency,out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text #melakukan request kedalam web target dan kemudian mengubahnya dalam bentuk text
    soup = BeautifulSoup(content,'html.parser') #disini memparse/menampilkan data target dalam bentuk html yang akan ditampilkan didalam text nanti
    currency = soup.find('span',class_='ccOutputRslt').get_text() #menampilkan data tertentu dlm bentuk text,jika ingin menampilkan dlm bentuk html hilangkan get_text()nya
    print(soup) #mencetak hasil scrapping
    print(currency) #menampilkan hasil scrapping tertentu


get_currency('INR','USD')
