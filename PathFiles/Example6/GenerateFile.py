#Membuat file banyak sekaligus

from pathlib import Path

root_dir = Path('d:/python/Automation/RestAPI-Example/PathFiles/Example6/files/')

for i in range(10, 21): #untuk generate file dari 10-20,21 disini adalah maximal angka yg akan dibuat jadi disini hanya sampai 20 tdk boleh sampai 21
  filename = str(i) + '.txt' #generate file dari 10-20 dengan format .txt
  filepath = root_dir / Path(filename)
  filepath.touch() #perintah untuk membuat suatu file
