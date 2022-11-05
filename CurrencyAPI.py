#import framework flask dan jsonify

from flask import Flask,jsonify

#import package beautifulsoap
from bs4 import BeautifulSoup

#import package requests
import requests

#membuat function untuk menampung data yang akan dipanggil dalam bentuk json
def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content,'html.parser')
    rate = soup.find("span",class_="ccOutputRslt").get_text()
    rate =float(rate[:-4])

    return rate

app = Flask(__name__)


#memasang route web agar website tampil dihalaman home/utama
@app.route('/')

#memuat function home untuk menampung data ke halaman utama
def home():
    return '<h1>Currency Rate API</h1><p>Example URL: /api/v1/usd-eur</p>'

#memasang route untuk meangalihkan halaman home kedalam page yg telah diatur di function home diatas
@app.route('/api/v1/<in_cur>-<out_cur>')

#membuat function untuk menampung data kedalam json
def api(in_cur,out_cur):
    rate = get_currency(in_cur,out_cur)
    result_dictionary ={'input_currency':in_cur,'output_currency':out_cur,'rate':rate}
    return jsonify(result_dictionary)

app.run(host='0.0.0.0')