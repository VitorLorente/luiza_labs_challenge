import json
import requests

api_url = "http://challenge-api.luizalabs.com/api/product/a0e4aa47-b17c-f266-f4d6-aba26ec085aa"

response = requests.get(api_url)

print(response.content.decode('utf-8'))