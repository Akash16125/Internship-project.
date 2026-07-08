import mysql.connector
from mysql.connector import Error


class Database:

    def connect(self):
        try:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Akash@123",
                database="garage_db1"
            )

            if con.is_connected():
                return con

        except Error as e:
            print("Database Connection Error:", e)
            return None