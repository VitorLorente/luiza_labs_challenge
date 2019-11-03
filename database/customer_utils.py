from .database import get_customer_list, get_customer, post_customer
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
    print(data_items[0])
    for i in range(len(data_items)-1):
        query_string += f"{data_items[i][0]} = '{data_items[i][1]}', "
    
    query_string += f"""{data_items[-1][0]} = '{data_items[-1][1]}'"""
    query_string += f'''
    WHERE id = {pk}
    RETURNING id;
    '''
    return query_string


def resolve_routes_post_customer(path:str, data:json):
    splited_path = path.split('/')
    splited_path = list(filter(lambda x: x != '', splited_path))
    path_length = len(splited_path)

    if path_length == 2 and splited_path[0] == 'cliente' and splited_path[-1] == 'create':
        query = query_post_customer(data)
        redirect_path = post_customer(query)
        return redirect_path
    
    elif path_length == 3 and splited_path[0] == 'cliente' and splited_path[-1] == 'update':
        try:
            int(splited_path[1])
            query = query_put_customer(splited_path[1], data)
            redirect_path = post_customer(query)
            return redirect_path
        except ValueError:
            return 404


def resolve_routes_get_customer(path:str):
    splited_path = path.split('/')
    splited_path = list(filter(lambda x: x != '', splited_path))
    path_length = len(splited_path)

    if path_length == 1:
        # get customer list
        query = query_get_customer_list()
        query_result = get_customer_list(query)

        return serialize_get_customer_list(query_result)

    elif path_length == 2 and splited_path[-1] != 'favorites-list':
        # Get customer
        customer_pk = splited_path[-1]
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