#Praktek membuat website menggunakan Framework Flask

from flask import Flask, render_template, request

app = Flask(__name__) #inisialisasi nama project yg akan dibuat

@app.route('/') #membuat routing dengan nama default index
def home():
  print("Get request string")
  return render_template('index.html')


@app.route('/', methods = ['POST'])
def home_post():
  dim1 = request.form['first_dim'] #firms_dim dll adalah sebuah tag name yg diambil dari htmlnya dimana ini bertujuan akan mengirimkan hasil request yg diinputkan pada tag htmlnya yg kemudian dari sini akan memberikan response
  dim2 = request.form['second_dim']
  dim3 = request.form['third_dim']
  volume = float(dim1) * float(dim2) * float(dim3)
  print()

  print("Get post request")
  return render_template('index.html', output=volume, dim_1=dim1, dim_2=dim2, dim_3=dim3)#dim_1,2,3 merupakan nama variable yg akan dimasukan kedalam tag html biar valuenya bisa muncul

app.run(host='0.0.0.0') #merender hasil codingan diatas yg akan dijalankan dengan alamat ip localhost yg sedang digunakan
