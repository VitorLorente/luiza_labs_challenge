from .database import get_customer_list, get_customer, post_customer, delete_customer
import json

def query_get_customer(pk:str) -> str:
    query_string = f'''
    SELECT * FROM customer WHERE id = {pk}; 
    '''
    return query_string

def query_get_customer_list() -> str:
    return 'SELECT * FROM customer;'

def query_post_customer(data:json) -> str:
    query_string = f'''
    INSERT INTO customer(name, email)
    VALUES  ('{data['name']}', '{data['email']}')
    RETURNING id;
    '''
    return query_string

def query_put_customer(pk:str, data:dict) -> str:
    query_string = '''
    UPDATE customer
    SET '''
    data_items = list(data.items())
    for i in range(len(data_items)-1):
        query_string += f"{data_items[i][0]} = '{data_items[i][1]}', "
    
    query_string += f"""{data_items[-1][0]} = '{data_items[-1][1]}'"""
    query_string += f'''
    WHERE id = {pk}
    RETURNING id;
    '''
    return query_string

def query_delete_customer(pk:str) -> str:
    query_string = f'''
    DELETE FROM customer
    WHERE id = {pk}
    '''
    return query_string


def resolve_routes_post_customer(path:str, data:json):
    splitted_path = path.split('/')
    splitted_path = list(filter(lambda x: x != '', splitted_path))
    path_length = len(splitted_path)

    if path_length == 2 and splitted_path[0] == 'cliente' and splitted_path[-1] == 'create':
        query = query_post_customer(data)
        redirect_path = post_customer(query)
        response = {
            'action': 'create',
            'redirect_path': redirect_path
        }
        return response
    
    elif path_length == 3 and splitted_path[0] == 'cliente' and splitted_path[-1] == 'update':
        try:
            int(splitted_path[1])
            query = query_put_customer(splitted_path[1], data)
            redirect_path = post_customer(query)
            response = {
                'action': 'update',
                'redirect_path': redirect_path
            }
            return response
        except ValueError:
            return 404

    elif path_length == 3 and splitted_path[0] == 'cliente' and splitted_path[-1] == 'delete':
        try:
            int(splitted_path[1])
            query = query_delete_customer(splitted_path[1])
            delete_customer(query)
            response = {
                "action": "delete",
                "status": f"Customer {splitted_path[1]} removed"
            }
            return response
        except ValueError:
            return 404


def resolve_routes_get_customer(path:str):
    splitted_path = path.split('/')
    splitted_path = list(filter(lambda x: x != '', splitted_path))
    path_length = len(splitted_path)

    if path_length == 1 and splitted_path[0] == 'cliente':
        # get customer list
        query = query_get_customer_list()
        query_result = get_customer_list(query)

        return serialize_get_customer_list(query_result)

    elif path_length == 2 and splitted_path[-1] != 'favorites-list':
        # Get customer
        customer_pk = splitted_path[-1]
        query = query_get_customer(customer_pk)
        query_result = get_customer(query)

        return serialize_get_customer(query_result)

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

def serialize_get_customer(query_result):
    serialized_data = {
        'id': query_result[0],
        'name': query_result[1],
        'email': query_result[2]
    }

    return json.dumps(serialized_data)