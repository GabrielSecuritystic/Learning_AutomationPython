#Belajar cara Automation Email sender Secara Berkala

#import dulu library yang dibutuhkan
import yagmail
import os
import time

sender = 'sender@gmail.com' #email pengirim
receiver = 'receiver@gmail.com' #email penerima

subject = 'Isi Subject atau Judul Pesan'

content = """Dibagian ini merupakan isi pesan yang akan dikirim ke email penerima"""


while True:
  yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
  yag.send(to=receiver, subject=subject, contents=content)
  print("Email Sent!")
  time.sleep(60) #disini akan memberi jeda setiap 60detik atau satu menit untuk melakukan pengiriman pesan ke email penerima
