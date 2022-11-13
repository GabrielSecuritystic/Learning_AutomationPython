#import package yg dibutuhkan

import yagmail
import os
import time
from datetime import datetime as dt

sender ="yourmail@mail.com" #email pengirim
receiver = "receiver@mail.com" #email penerima

subject ="""
Judul Pesan
"""

Content = """Isi pesan yg akan dikirim ke email penerima/receiver"""

while True:
    now = dt.now()
    if now.hour == 13 and now.minute == 18: #ketetrangan bahwa email akan dikirim ketika jam 13.18 setiap harinya
        yag = yagmail.SMTP(user=sender,password=os.getenv('PASSWORD'))
        yag.send(to=receiver,subject=subject,contents=Content)
        print("Email Terkirim")
        time.sleep(60) #memberikan jeda setiap kali mengirim email