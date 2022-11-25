#latihan python GUI menggunakan library PyQt5

from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout
from PyQt5.QtWidgets import QLabel,QPushButton,QLineEdit

#import package beautifulsoap
from bs4 import BeautifulSoup

#import package requests
import requests

#membuat function untuk menampung data yang akan dipanggil dalam bentuk json
def get_currency(in_currency='USD', out_currency='EUR'):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content,'html.parser')
    rate = soup.find("span",class_="ccOutputRslt").get_text()
    rate =float(rate[:-4])

    return rate

def show_currency():
    input_text = float(text.text())
    rate = get_currency()
    output = round(input_text * rate, 2)
    output_label.setText(str(output))

app = QApplication([])
window =QWidget()
window.setWindowTitle("Pengenalan PyQt untuk membuat aplikasi GUI dengan Python")

layout = QHBoxLayout()

btn = QPushButton('Convert')
layout.addWidget(btn)
btn.clicked.connect(show_currency)

output_label = QLabel()
layout.addWidget(output_label)

text =QLineEdit()
layout.addWidget(text)


window.setLayout(layout)
window.show()
app.exec()