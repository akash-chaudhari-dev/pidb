import requests

url = 'http://localhost:8000/api/items/?id=1'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for item in data:
        print(item['name'], "-", item['description'])
else:
    print("Error:", response.status_code)
