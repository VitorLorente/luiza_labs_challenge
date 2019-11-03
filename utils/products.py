import requests
import json

def check_product(pk:str) -> dict:
    api_url = f"http://challenge-api.luizalabs.com/api/product/{pk}"
    response = requests.get(api_url)

    return response.status_code == 200

def get_product(pk:str) -> dict:
    api_url = f"http://challenge-api.luizalabs.com/api/product/{pk}"
    response = requests.get(api_url)

    return [json.loads(response.content)]