#Praktikum Automation Email menggunakan daftar contact

#Import package yg akan digunakan
import yagmail
import os
import pandas #package ini diguankan untuk menganalisa sebuah data

sender = 'sender@mail.com' #email pengirim pesan
receiver = 'receiver@mail.com' #email tujuan

subject = """Judul Email yang akan Dikirim"""

content = """Isi pesan yg akan dikirim"""

yag = yagmail.SMTP(user=sender,password=os.getenv('PASSWORD'))
df = pandas.read_csv('contacts.csv')

for index,row in df.iterrows():
    content = f"""Hi {row['name']} test"""#mengambil nama pemilik email yg ada difile contacts.csv
    yag.send(to=row['email'],subject=subject,contents=content)
    print("Email terkirim")

