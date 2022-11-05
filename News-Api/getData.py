#import package requests
import requests

#membuat function dengan default parameter untuk getData berdasarkan hasil inputan
def get_news(topic,from_date,to_date,language='en', api_key='717652869d454fcbb886b6dcf9246112'):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}8&sortBy=popularity&language={language}&apiKey={api_key}'
    r = requests.get(url) #memanggil function request
    content = r.json() #menampilkan data berdasarkan request kedalam bentuk json
    articles = content['articles'] #memanggil data yang memiliki key articles
    result = [] #menampilkan data kedalam array
    for article in articles:
        result.append(f"TITLE\n'{article['title']},'\nDESCRIPTION\n',{article['description']}") #menambahkkan kata kunci title/judul dan description untuk mendapatkan data articles
        return result #mengembalikan data yang telah dipanggil kedalam variable result agar berbentuk array

print(get_news(topic='space', from_date='2022-10-11', to_date='2022-10-11')) #menginputkan request data yang akan didapatkan
