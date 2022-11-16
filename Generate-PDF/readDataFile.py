#Praktikum cara membaca isi sebuah file

#Import package yang dibutuhkan
import fitz

with fitz.open("Generate-PDF/Generate-PDF/students.pdf") as pdf:
  text = ''
  for page in pdf:
    text = text + page.get_text()
    print(text)