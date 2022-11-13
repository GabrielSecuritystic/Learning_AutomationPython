#Belajar cara Automation mengirim email

#import library yagmail(jika belum ada harus install dulu)
import yagmail

import os

sender = 'sender@gmail.com' #email pengirim
receiver = 'receiver@hempyl.com' #email penerima

subject = 'Isi Subject atau Judul Pesan'

content = """Dibagian ini merupakan isi pesan yang akan dikirim ke email penerima"""

#configurasi smtp
yag = yagmail.SMTP(user=sender,password=os.getenv('PASSWORD'))
yag.send(to=receiver,subject=subject,contents=content)
print("Email Terkirim") #untuk menandai bahwa pesan sudah dikirim ke email penerima

