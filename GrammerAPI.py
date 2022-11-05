import requests
import json

url = 'https://api.languagetool.org/v2/check' #memanggil web target api
data= {
	'text':'Tis is a nixe day!',
	'language':'auto'
}

response = requests.post(url,data=data)
# print(response.text)

#menampung data hasil get data api lewat json
result = json.loads(response.text)
print(result)