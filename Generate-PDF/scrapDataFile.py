#Praktikum Cara Scrap data dari suatu file

#import package yang dibutuhkan

import tabula

table = tabula.read_pdf('Generate-PDF/Generate-PDF/weather.pdf',pages=1)
print(type(table[0])) #scrap data pada table ke.0

table[0].to_csv('Generate-PDF/Generate-PDF/scrapData.csv',index=None) #scrap data pada table index ke.0