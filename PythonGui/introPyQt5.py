#latihan python GUI menggunakan library PyQt5

from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout
from PyQt5.QtWidgets import QLabel,QPushButton,QLineEdit

def make_sentence():
    input_text = text.text()
    output_label.setText(input_text.capitalize() + '.')

app = QApplication([])
window =QWidget()
window.setWindowTitle("Pengenalan PyQt untuk membuat aplikasi GUI dengan Python")

layout = QHBoxLayout()

btn = QPushButton('Make')
layout.addWidget(btn)
btn.clicked.connect(make_sentence)

output_label = QLabel()
layout.addWidget(output_label)

text =QLineEdit()
layout.addWidget(text)


window.setLayout(layout)
window.show()
app.exec()