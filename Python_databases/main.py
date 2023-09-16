import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

DROP_TABLES_USERS = "DROP TABLE IF EXISTS users"

USERS_TABLES = """CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""

users =[
    ("user1", "password", "user1@gmail.com"),
    ("user2", "password", "user2@gmail.com"),
    ("user3", "password", "user3@gmail.com"),
    ("user4", "password", "user4@gmail.com"),
    ("user5", "password", "user5@gmail.com"),

]

if __name__ == "__main__":

    try:
        connect = pymysql.Connect(
            host=("localhost"), 
            port=3306, 
            user=os.getenv("USER_MYSQL"), 
            passwd=os.getenv("PASSWORD_MYSQL"), 
            db=os.getenv("DB_MYSQL")
        )
    
        with connect.cursor() as cursor:

            cursor.execute(DROP_TABLES_USERS)
            cursor.execute(USERS_TABLES)
    
            query = "INSERT INTO users(username, password, email) VALUES(%s, %s, %s)"
   
            cursor.executemany(query, users)
            connect.commit()

            query = "DELETE FROM users WHERE id = %s"
            
            cursor.execute(query, (5,))
            connect.commit()

    except pymysql.err.OperationalError as err:
        print("No fue posible realizar la conexión")
        print(err)

    finally:

        connect.close()

        print("Conexión finalizada de forma exitosa")
