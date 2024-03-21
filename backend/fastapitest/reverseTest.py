# import requests

# url = "http://127.0.0.1:8000/reverse_string"
# data = "Hello World"
# response = requests.post(url, json=data)
# print(response.json())
import requests

url = "http://127.0.0.1:8000/reverse_string"
data = "Hello World"
response = requests.post(url, json=data)
print(response.json())
