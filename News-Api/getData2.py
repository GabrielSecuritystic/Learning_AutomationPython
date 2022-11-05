#import package requests
import requests

#membuat function untuk mengambil data berita berdasarkan country dan berita terbaru
def get_news(country,api_key='717652869d454fcbb886b6dcf9246112'):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []

#membuat looping untuk memanggil data
    for articles in articles:
        results.append(f"TITLE\n'{articles['title']},'\nDESCRIPTION\n',{articles['description']}")
        return results

print(get_news(country='us'))
