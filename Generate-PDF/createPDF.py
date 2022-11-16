#import library fpdf untuk membuat file pdf dengan python

from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4') #mengatur format halaman yg akan dibuat
pdf.add_page() #function untuk membuat halaman pdf

pdf.image('Generate-PDF/Generate-PDF/flag.png',w=80,h=50) #menambahkan gambar dan format gambar yg akan ditambahkan

pdf.set_font(family='Times',style='B',size=24) #mengatur font

pdf.cell(w=0,h=50,txt="Bendera Indonesia",align='C',ln=1) #mengatur jarak antar cell/layouting untuk merapikan halaman

pdf.set_font(family='Times',size=12)


txt1="""Ini adalah bendera Negara indonesia"""
pdf.multi_cell(w=0,h=15,txt=txt1) #mengatur jarak cell pada text pertama/txt1

pdf.set_font(family='Times',style='B',size=14)
pdf.cell(w=100,h=25,txt='Kingdom:')

pdf.set_font(family='Times', size=14)
pdf.cell(w=100, h=25, txt='Animalia', ln=1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=25, txt='Phylum:')

pdf.set_font(family='Times', size=14)
pdf.cell(w=100, h=25, txt='Chordata', ln=1)


pdf.output('Generate-PDF/Generate-PDF/output.pdf') #generate file pdf berdasarkan data yg dimasukan
