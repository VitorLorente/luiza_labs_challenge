def query_get_customer(pk:str) -> str:
    query_string = f'''
    SELECT * FROM customer WHERE id = {pk}; 
    '''
    return query_string

def query_get_customer_list() -> str:
    return 'SELECT * FROM customer;'

def query_post_customer(data:dict) -> str:
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

def query_create_favorite_product(pk_customer:str, pk_product:str) -> str:
    query_string = f'''
    INSERT INTO CustomerFavoriteProduct (id_customer, id_product)
    VALUES ('{pk_customer}', '{pk_product}')
    RETURNING id_customer;
    '''
    return query_string

def query_get_favorites_products(pk_customer:str) -> str:
    query_string = f'''
    SELECT id_product, id_customer, name, email
    FROM CustomerFavoriteProduct
    INNER JOIN customer ON customer.id = id_customer
    WHERE id_customer = {pk_customer};
    '''
    return query_string