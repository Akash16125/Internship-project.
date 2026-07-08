from database import Database
from datetime import date


class Billing:

    def __init__(self):
        self.db = Database()
        self.con = self.db.connect()

        if self.con:
            self.cursor = self.con.cursor()

    def generate_bill(self):

        vehicle_id = int(input("Enter Vehicle ID: "))

        # Check whether vehicle exists
        sql = "SELECT * FROM vehicles WHERE vehicle_id=%s"
        self.cursor.execute(sql, (vehicle_id,))
        result = self.cursor.fetchone()

        if result is None:
            print("Vehicle ID not found.")
            return

        print("\n------ Services ------")
        print("1. Car Wash           ₹500")
        print("2. Oil Change         ₹1000")
        print("3. Brake Service      ₹1500")
        print("4. Wheel Alignment    ₹800")
        print("5. Full Service       ₹5000")

        choice = int(input("Select Service: "))

        if choice == 1:
            service = "Car Wash"
            amount = 500
        elif choice == 2:
            service = "Oil Change"
            amount = 1000
        elif choice == 3:
            service = "Brake Service"
            amount = 1500
        elif choice == 4:
            service = "Wheel Alignment"
            amount = 800
        elif choice == 5:
            service = "Full Service"
            amount = 5000
        else:
            print("Invalid Choice")
            return

        sql = """
        INSERT INTO bills(vehicle_id, service, amount, bill_date)
        VALUES(%s, %s, %s, %s)
        """

        value = (vehicle_id, service, amount, date.today())

        self.cursor.execute(sql, value)
        self.con.commit()

        print("\n------ Bill Generated ------")
        print("Vehicle ID :", vehicle_id)
        print("Service    :", service)
        print("Amount     : ₹", amount)
        print("Date       :", date.today())
        print("Bill Generated Successfully.")

    def view_bill(self):

        sql = """
        SELECT
            bills.bill_id,
            customers.customer_name,
            vehicles.vehicle_number,
            bills.service,
            bills.amount,
            bills.bill_date
        FROM bills
        INNER JOIN vehicles
            ON bills.vehicle_id = vehicles.vehicle_id
        INNER JOIN customers
            ON vehicles.customer_id = customers.customer_id
        """

        self.cursor.execute(sql)

        data = self.cursor.fetchall()

        print("\n------ Bill List ------")

        for row in data:
            print("Bill ID         :", row[0])
            print("Customer Name   :", row[1])
            print("Vehicle Number  :", row[2])
            print("Service         :", row[3])
            print("Amount          : ₹", row[4])
            print("Bill Date       :", row[5])
            print("-" * 35)