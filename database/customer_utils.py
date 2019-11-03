from .database import get_customer_list
import json

def query_get_customer(pk:str) -> str:
    query_string = f'''
    SELECT * FROM customer WHERE id = {pk}; 
    '''
    return query_string

def query_get_customer_list() -> str:
    return 'SELECT * FROM customer;'


def resolve_routes_get_customer(path:str):
    splited_path = path.split('/')
    splited_path = list(filter(lambda x: x != '', splited_path))
    path_length = len(splited_path)
    if path_length == 1:
        query = query_get_customer_list()
        query_result = get_customer_list(query)
        return serialize_get_customer_list(query_result)
    elif path_length == 2 and splited_path[-1] != 'favorites-list':
        # Get customer
        customer_pk = splited_path[-1]
        query = query_get_customer(customer_pk)
        pass
    else:
        # get favorite-list
        pass


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