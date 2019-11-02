import psycopg2
try:
    connection = psycopg2.connect(user="postgres_luiza_labs",
                                  password="desafio_luiza_labs",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="luiza_labs_db")

    cursor = connection.cursor()

    # Criando tabelas
    # Cliente
    cursor.execute("""CREATE TABLE Customer(
        id serial PRIMARY KEY,
        name varchar (50) NOT NULL,
        email varchar (50) NOT NULL,
        CONSTRAINT UNIQUE (email)
        );""")

    # Produto
    cursor.execute("""CREATE TABLE Product(
        id serial PRIMARY KEY,
        title varchar (30) NOT NULL,
        brand varchar (30) NOT NULL,
        image varchar (30) NOT NULL,
        price float (2) NOT NULL,
        reviewScore float(2) NOT NULL,
        );""")

    # Criando 10 clientes iniciais
    for i in range(1, 10):
        cursor.execute(f"INSERT INTO Customer(name, email) VALUES ('Cliente {i}', 'cliente{i}@luizalabs.com');")

    # Criando 5 produtos
    cursor.execute("""INSERT INTO Product(title, brand, image, price, reviewScore)
    VALUES ('TV 29 polegadas', 'Samsung', 'imgs/tvs/samsung/29-polegadas.jpeg', 1000.00, 9.50),
    ('iPhone 8 256GB Prata', 'apple', 'imgs/smartphones/apple/iphone8-256-prata.jpeg', 3149.91, 9.25);""")

    connection.commit()

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")