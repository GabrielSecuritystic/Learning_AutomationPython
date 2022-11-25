#latihan python GUI menggunakan library PyQt5

from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout
from PyQt5.QtWidgets import QLabel,QPushButton,QLineEdit,QComboBox

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
    in_currency = in_combo.currentText()
    target_currency = target_combo.currentText()
    print(in_currency, target_currency)
    rate = get_currency(in_currency,target_currency)
    output = round(input_text * rate, 2)
    message = f'{input_text} {in_currency}  is {output} {target_currency}'
    output_label.setText(str(message))

app = QApplication([])
window =QWidget()
window.setWindowTitle("Pengenalan PyQt untuk membuat aplikasi GUI dengan Python")

layout = QVBoxLayout()

in_combo = QComboBox()
currencies = ['USD','EUR','IDR']
in_combo.addItems(currencies)
layout.addWidget(in_combo)

target_combo = QComboBox()
target_combo.addItems(currencies)
layout.addWidget(target_combo)

text = QLineEdit()
layout.addWidget(text)

btn = QPushButton('Convert')
layout.addWidget(btn)
btn.clicked.connect(show_currency)

output_label = QLabel('')
layout.addWidget(output_label)

text =QLineEdit()
layout.addWidget(text)


window.setLayout(layout)
window.show()
app.exec()