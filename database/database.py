import psycopg2
from env import env_datas

def make_connection():
    connection = psycopg2.connect(
        user=env_datas['user'],
        password=env_datas['psswd'],
        host=env_datas['host'],
        port=env_datas['port'],
        database=env_datas['db']
    )

    return connection


def get_customer_list(query:str) -> list:
    connection = make_connection()

    cursor = connection.cursor()
    cursor.execute(query)
    customers = cursor.fetchall()
    return customers

def get_customer(query:str) -> tuple:
    connection = make_connection()

    cursor = connection.cursor()
    cursor.execute(query)
    customer = cursor.fetchone()
    return customer

def post_customer(query:str) -> str:
    connection = make_connection()

    cursor = connection.cursor()
    cursor.execute(query)
    customer_id = cursor.fetchone()[0]
    connection.commit()
    redirect_path = f'/cliente/{customer_id}'
    return redirect_path

def delete_customer(query:str):
    connection = make_connection()

    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

def create_favorite_product(query:str) -> str:
    connection = make_connection()

    cursor = connection.cursor()
    cursor.execute(query)
    customer_id = cursor.fetchone()[0]
    connection.commit()
    redirect_path = f'/cliente/{customer_id}/favorite-products'
    return redirect_path

def get_favorites_products(query:str) -> list:
    connection =make_connection()

    cursor = connection.cursor()
    cursor.execute(query)
    customers = cursor.fetchall()
    return customers