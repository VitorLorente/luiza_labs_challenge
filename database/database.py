import psycopg2
# try:
#     connection = psycopg2.connect(user="postgres_luiza_labs",
#                                   password="desafio_luiza_labs",
#                                   host="127.0.0.1",
#                                   port="5432",
#                                   database="luiza_labs_db")

#     cursor = connection.cursor()
#     # Print PostgreSQL Connection properties
#     print ( connection.get_dsn_parameters(),"\n")

#     # Print PostgreSQL version
#     cursor.execute("INSERT INTO customer(name, email) VALUES ('Vitor Lorente', 'vitorlorente@luizalabs.com');")
#     cursor.execute("SELECT name, email FROM customer;")
#     record = cursor.fetchall()
#     string_return = ""
#     for row in record:
#         string_return += f"{row}\n"
#     print(string_return)
#     connection.commit()

# except (Exception, psycopg2.Error) as error :
#     print ("Error while connecting to PostgreSQL", error)
# finally:
#     #closing database connection.
#         if(connection):
#             cursor.close()
#             connection.close()
#             print("PostgreSQL connection is closed")


def get_customer_list(query):
    connection = psycopg2.connect(user="postgres_luiza_labs",
                                  password="desafio_luiza_labs",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="luiza_labs_db")

    cursor = connection.cursor()
    cursor.execute(query)
    customers = cursor.fetchall()
    return customers