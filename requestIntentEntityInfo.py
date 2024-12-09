import requests

print("Hello! What is your request?")
x = input()
url = "http://0.0.0.0:5005/model/parse"
r = requests.post(url, json = {"text":x})
print(r)

print(r.json())