import json
from database.database import (
    get_customer_list,
    get_customer,
    post_customer,
    delete_customer,
    create_favorite_product,
    get_favorites_products
)
from utils.queries import (
    query_get_customer,
    query_get_customer_list,
    query_post_customer,
    query_put_customer,
    query_delete_customer,
    query_create_favorite_product,
    query_get_favorites_products
)
from utils.serializers import (
    serialize_get_customer_list,
    serialize_get_customer,
    serialize_get_favorites_products
)
from utils.products import check_product

def normalize_path(path:str) -> list:
    splitted_path = path.split('/')
    splitted_path = list(filter(lambda x: x != '', splitted_path))
    path_length = len(splitted_path)
    return splitted_path, path_length

def resolve_routes_post_customer(path:str, data:json):
    splitted_path, path_length = normalize_path(path)

    if path_length == 2 and splitted_path[0] == 'cliente' and splitted_path[-1] == 'create':
        query = query_post_customer(data)
        redirect_path = post_customer(query)
        response = {
            'action': 'create',
            'message': redirect_path,
            'status': 200
        }
        return response
    
    elif path_length == 4 and splitted_path[0] == 'cliente' and splitted_path[2] == 'favorite-products' and splitted_path[-1] == 'create':
        try:
            int(splitted_path[1])
            if check_product(data['id_product']):
                query = query_create_favorite_product(splitted_path[1], data['id_product'])
                redirect_path = create_favorite_product(query)
                response = {
                    "action": "create",
                    "message": redirect_path,
                    "status": 200
                }
                return response
            else:
                response = {
                    "action": "create",
                    "message": "Product does not exist.",
                    "status": 404
                }
                return response
        except ValueError:
            response = {
                "action": "create",
                "message": "Not found.",
                "status": 404
            }
            return response

    response = {
        "action": "create",
        "message": "Not found.",
        "status": 404
    }
    return response

def resolve_routes_put_customer(path:str, data:dict):
    splitted_path, path_length = normalize_path(path)

    if path_length == 3 and splitted_path[0] == 'cliente' and splitted_path[-1] == 'update':
        try:
            int(splitted_path[1])
            query = query_put_customer(splitted_path[1], data)
            redirect_path = post_customer(query)
            response = {
                'action': 'update',
                'message': redirect_path,
                'status': 200
            }
            return response
        except ValueError:
            response = {
                "action": "create",
                "message": "Not found.",
                "status": 404
            }
            return response
    response = {
        "action": "create",
        "message": "Not found.",
        "status": 404
    }
    return response

def resolve_routes_delete_customer(path:str):
    splitted_path, path_length = normalize_path(path)

    if path_length == 3 and splitted_path[0] == 'cliente' and splitted_path[-1] == 'delete':
        try:
            int(splitted_path[1])
            query = query_delete_customer(splitted_path[1])
            delete_customer(query)
            response = {
                "action": "delete",
                "message": f"Customer {splitted_path[1]} removed",
                "status": 200
            }
            return response
        except ValueError:
            response = {
                "action": "create",
                "message": "Not found.",
                "status": 404
            }
            return response
    response = {
        "action": "create",
        "message": "Not found.",
        "status": 404
    }
    return response

def resolve_routes_get_customer(path:str):
    splitted_path, path_length = normalize_path(path)

    if path_length == 1 and splitted_path[0] == 'cliente':
        # get customer list
        query = query_get_customer_list()
        query_result = get_customer_list(query)

        return serialize_get_customer_list(query_result)

    elif path_length == 2 and splitted_path[0] == 'cliente' and splitted_path[-1] != 'favorites-list':
        # Get customer
        customer_pk = splitted_path[-1]
        query = query_get_customer(customer_pk)
        query_result = get_customer(query)

        return serialize_get_customer(query_result)

    elif path_length == 3 and splitted_path[0] == 'cliente' and splitted_path[-1] == 'favorites-list':
        # get favorite-list
        customer_pk = splitted_path[1]
        query = query_get_favorites_products(customer_pk)
        query_result = get_favorites_products(query)

        return serialize_get_favorites_products(query_result)