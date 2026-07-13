import mysql.connector
from mysql.connector import Error


class Database:

    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Akash@123",
                database="login_system"
            )

            self.cursor = self.connection.cursor(buffered=True)

        except Error as e:
            print("Database Connection Error:", e)

    def execute(self, query, values=None):
        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)

        if query.strip().upper().startswith(("INSERT", "UPDATE", "DELETE")):
            self.connection.commit()

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()