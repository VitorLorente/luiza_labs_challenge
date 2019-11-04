import psycopg2
from database.database import make_connection

def migrate(customers):
    try:
        connection = make_connection()

        cursor = connection.cursor()

        # Criando tabelas
        # Cliente
        cursor.execute("""CREATE TABLE Customer(
            id serial PRIMARY KEY,
            name varchar (50) NOT NULL,
            email varchar (50) NOT NULL,
            CONSTRAINT unique_customer_email UNIQUE (email)
            );""")

        cursor.execute("""CREATE TABLE CustomerFavoriteProduct(
            id_customer integer NOT NULL REFERENCES Customer(id),
            id_product varchar (37) NOT NULL,
            CONSTRAINT unique_product_per_customer PRIMARY KEY(id_customer, id_product)
            );""")

        if customers:
            for i in range(0, customers):
                cursor.execute(f"INSERT INTO Customer(name, email) VALUES ('Cliente {i+1}', 'cliente{i+1}@luizalabs.com');")

        print(f'\nTabelas criadas. Foram adicionados {customers} clientes.\n')

        connection.commit()

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")