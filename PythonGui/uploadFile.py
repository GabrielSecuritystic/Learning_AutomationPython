#Latihan Upload file dengan python menggunakan PyQt5

from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout
from PyQt5.QtWidgets import QLabel,QPushButton,QFileDialog
from PyQt5.QtCore import Qt

from pathlib import Path

#membuat function untuk mengaktifkan interactive clicked di button
def open_files():
    global filenames #membuat variable filenames menjadi variable global agar bisa diakses diluar scope function
    filenames, _ = QFileDialog.getOpenFileNames(window,'Select files')
    print(filenames)
    message.setText('\n'.join(filenames))


#membuat function untuk destroy atau delete file

def destroy_files():
     for filename in filenames:
        path = Path(filename)
        with open(path, 'wb') as file:
            file.write(b'')
        path.unlink()
     message.setText("Hapus file berhasil")

app = QApplication([])
window = QWidget()
window.setWindowTitle("File Upload and Destroyer")
layout = QVBoxLayout()

description = QLabel('Select the files you want to destroy.The files will be <font color="red">permanent</font>deleted')
layout.addWidget()

open_btn = QPushButton("Open Files")
open_btn.setToolTip('Open Files')
open_btn.setFixedWidth(100)
layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter)
open_btn.clicked.connect(open_files)

#membuat button untuk menghapus file yg sudah diupload
destroy_btn = QPushButton("Destroy Files")
destroy_btn.setFixedWidth(100)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)
destroy_btn.clicked.connect(destroy_files)

#menampilkan data yg akan diupload dan akan dihapus
message = QLabel('')
layout.addWidget(message)


window.setLayout(layout)
window.show()
app.exec()


