import json
import requests

api_url = "http://challenge-api.luizalabs.com/api/product/df22bfd5-7a47-0aaa-d28d-125d528318b4"

response = requests.get(api_url)

print(response.content.decode('utf-8'))
print(response.status_code)

def check_product(pk:str) -> dict:
    api_url = f"http://challenge-api.luizalabs.com/api/product/{pk}"
    response = requests.get(api_url)

    return {"status": response.status_code, "pk": pk}
