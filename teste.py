import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='api_demo',
                                         user='root',
                                         password='root')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()

        query = "select * from administradores"
        cursor.execute(query)
        adms = cursor.fetchall()

        print("===================")
        for item in adms:
            print(f"id: {item[0]}")
            print(f"email: {item[1]}")
            print(f"nome: {item[2]}")
            print(f"obs: {item[3]}")
            print(f"senha: {item[4]}")
            print("-------------------------")
        print("===================")

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")