#praktikum Membuat PDF dari data Excel

#import package yang dibutuhkan

import pandas
from fpdf import FPDF


df = pandas.read_excel('Generate-PDF/Generate-PDF/data.xlsx') #method untuk membaca data yg berupa excel

for index, row in df.iterrows():
  pdf = FPDF(orientation='P', unit='pt', format='A4') #mengisi sebuah constructor pada class FPDF berupa formatting layout
  pdf.add_page() #method untuk membuat sebuah halaman

  pdf.set_font(family='Times', style='B', size=24) #methd untuk mengatur sebuah font yang akan digunakan
  pdf.cell(w=0, h=50, txt=row['name'], align='C', ln=1) #mengambil data nama dari file yg dipanggil

  for column in df.columns[1:]:
    pdf.set_font(family='Times', style='B', size=14)
    pdf.cell(w=100, h=25, txt=f"{column.title()}:") #mengambil data judul dari file yg dipanggil

    pdf.set_font(family='Times', size=14)
    pdf.cell(w=100, h=25, txt=row[column], ln=1)


  pdf.output(f"Generate-PDF/Generate-PDF/{row['name']}.pdf") #generate nama file pdf berdasarkan nama yg diambil pada file tersebut