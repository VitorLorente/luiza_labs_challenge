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
        CONSTRAINT unique_customer_email UNIQUE (email)
        );""")

    # Produto
    cursor.execute("""CREATE TABLE Product(
        id serial PRIMARY KEY,
        title varchar (100) NOT NULL,
        brand varchar (30) NOT NULL,
        image varchar (100) NOT NULL,
        price float (2) NOT NULL,
        reviewScore float(2) NOT NULL
        );""")

    # Criando 10 clientes iniciais
    for i in range(0, 1000):
        cursor.execute(f"INSERT INTO Customer(name, email) VALUES ('Cliente {i+1}', 'cliente{i+1}@luizalabs.com');")

    # Criando 5 produtos
    cursor.execute("""INSERT INTO Product(title, brand, image, price, reviewScore)
    VALUES ('TV 29 polegadas', 'Samsung', 'imgs/tvs/samsung/29-polegadas.jpeg', 1000.00, 9.50),
    ('iPhone 8 256GB Prata', 'Apple', 'imgs/smartphones/apple/iphone8-256-prata.jpeg', 3149.91, 9.00),
    ('Relógio Feminino Mondaine Analógico', 'Mondaine', 'imgs/relogios/mondaine/relógio-feminino-mondaine-analógico.jpeg', 132.90, 10.00),
    ('Faqueiro Inox Búzios 72 Peças', 'Tramontina', 'imgs/faqueiros/tramontina/faqueiro-inox-buzios-72-peças.jpeg', 109.00, 9.25),
    ('Papel Higiênico Folha Dupla', 'Neve', 'imgs/papel-higienico/neve/papel-higienico-folha-dupla.jpeg', 17.90, 9.25),
    ('Cômoda Infantil 2 Gavetas', 'Art In Móveis', 'imgs/comoda/art-in-moveis/comoda-infantil-2-gavetas.jpeg', 377.06, 9.80),
    ('Aparelho de Barbear', 'Gillette', 'imgs/aparelho-barbear/gillete/aparelho-de-barbear.jpeg', 112.20, 10.00),
    ('Loção Pós-Barba Gillette Sensitive Skin', 'Gillette', 'imgs/locao-pos-barba/gillete/locao-pos-barba.jpeg', 29.90, 9.90),
    ('Ferro de Passar a Vapor e a Seco', 'Arno', 'imgs/ferro-de-passar/arno/ferro-de-passar-a-vapor-e-a-seco.jpeg', 151.91, 7.00),
    ('Cabeceira Solteiro', 'Madesa', 'imgs/cabeceira-solteiro/madesa/cabeceira-solteiro.jpeg', 100.71, 6.0);""")

    connection.commit()

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")