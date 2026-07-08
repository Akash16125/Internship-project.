from database import Database


class Customer:

    def __init__(self):
        self.db = Database()
        self.con = self.db.connect()

        if self.con:
            self.cursor = self.con.cursor()

    def add_customer(self):

        name = input("Enter Customer Name: ")
        mobile = input("Enter Mobile Number: ")

        sql = """
        INSERT INTO customers(customer_name, mobile)
        VALUES(%s, %s)
        """

        value = (name, mobile)

        self.cursor.execute(sql, value)
        self.con.commit()

        print("Customer Added Successfully.")

    def view_customer(self):

        sql = "SELECT * FROM customers"

        self.cursor.execute(sql)

        data = self.cursor.fetchall()

        print("\n------ Customer List ------")

        for row in data:
            print(row)

    def add_vehicle(self):

        customer_id = int(input("Enter Customer ID: "))

        # Check whether customer exists
        sql = "SELECT * FROM customers WHERE customer_id=%s"
        self.cursor.execute(sql, (customer_id,))
        result = self.cursor.fetchone()

        if result is None:
            print("Customer ID not found.")
            return

        vehicle_number = input("Enter Vehicle Number: ")
        vehicle_name = input("Enter Vehicle Name: ")

        sql = """
        INSERT INTO vehicles(customer_id, vehicle_number, vehicle_name)
        VALUES(%s, %s, %s)
        """

        value = (customer_id, vehicle_number, vehicle_name)

        self.cursor.execute(sql, value)
        self.con.commit()

        print("Vehicle Added Successfully.")

    def view_vehicle(self):

        sql = """
        SELECT
            vehicles.vehicle_id,
            customers.customer_name,
            vehicles.vehicle_name,
            vehicles.vehicle_number
        FROM vehicles
        INNER JOIN customers
        ON customers.customer_id = vehicles.customer_id
        """

        self.cursor.execute(sql)

        data = self.cursor.fetchall()

        print("\n------ Vehicle List ------")

        for row in data:
            print(row)