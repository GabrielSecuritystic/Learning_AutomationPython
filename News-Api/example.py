#import package requests
import requests


r= requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-10-27&to=2022-2-28&sortBy=popularity&language=en&apiKey=717652869d454fcbb886b6dcf9246112')
content = r.json() #menampilkan data yang ada didalam variable r menjadi data json
print(type(content))
print(content['articles'][0]['description'])#artinya mengambil data articles pada index ke.0 dimana data yang akan diambil berupa description
