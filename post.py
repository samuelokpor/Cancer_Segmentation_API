import requests

url = "http://127.0.0.1:8000/"

payload = {}
files = [
    (('testimg.jpg', open('testimg.jpg', 'rb'), 'image/jpeg'))
]
headers = {
    'accept': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=files)

print(response.text)