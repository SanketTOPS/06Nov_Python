import requests

url="https://fakestoreapi.com/products"

req=requests.get(url)
data=req.json()
#print(data)

for i in data:
    print("ID:",i["id"])
    print("Title:",i["title"])
    print("Price:",i["price"])