import json
from utils.products import get_product

def serialize_get_customer_list(query_result):
    serialized_data = [
        {
            'id': customer[0],
            'name': customer[1],
            'email': customer[2]
        }
        for customer in query_result
    ]

    return json.dumps(serialized_data)

def serialize_get_customer(query_result):
    serialized_data = {
        'id': query_result[0],
        'name': query_result[1],
        'email': query_result[2]
    }

    return json.dumps(serialized_data)

def serialize_get_favorites_products(query_result):
    name = query_result[0][2]
    email = query_result[0][3]
    serialized_data = {
        'customer': {
            "name": name,
            "email": email
        },
        "products": [
            {
                "title": product["title"],
                "price": product["price"],
                "image": product["image"],
                "id": product["id"]
            }
            for item in query_result for product in get_product(item[0])
        ]
    }
    return json.dumps(serialized_data)