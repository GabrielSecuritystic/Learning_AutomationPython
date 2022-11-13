#Praktikum mengirim sebuah file dengan Automation Mail

#import package yg dibutuhkan
import yagmail
import os

sender = 'sender@mail.com' #email pengirim
receiver = 'receiver@mail.com' #alamat tujuan pengiriman email


subject = """Judul Pesan/email"""
content = ["""Isi pesan""",'file.txt']#mengirim sebuah file dengan email

yag = yagmail.SMTP(user=sender,password=os.getenv('PASSWORD'))
yag.send(to=receiver,subject=subject,contents=content)
print("Email terkirim")