#Praktikum Automation mengirim email dengan menambahkan sebuah file dan edit file

#import package yg akan digunakan
import yagmail
import os
import pandas

sender = 'sender@mail' #email pengirim
yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))


df = pandas.read_csv('data.csv')

def generate_file(filename,content):
    with open(filename, 'w') as file:
        file.write(str(content))

for index, row in df.iterrows():
  name = row['name']
  filename = name + ".txt" #ini akan mengenerate sebuah file dengan nama sebuah data yg diambil(dicontoh ini memanggil data nama)  dan dengan format .txt
  amount = row['amount'] #mengambil data amount yg ada difile data.csv yg dipanggil
  receiver_email = row['email'] #mengambil data email yang ada difile data.csv yg dipanggil,dimana email yg ada di file data.csv akan dikirimkan pesan oleh sender(pengirim email)

  generate_file(filename, amount)

  subject = "This is the subject!"
  contents = [f"""
  Hey, {name} you have to pay {amount}
  Bill is attached!""",
  filename,
  ]

  yag.send(to=receiver_email, subject=subject, contents=contents)
  print("Email Sent!")