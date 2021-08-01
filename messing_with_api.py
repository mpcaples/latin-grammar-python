import requests

url = 'https://www.latin-is-simple.com/api/vocabulary/'

r = requests.get(url=url)
data_test = r.json()

print(data_test)

