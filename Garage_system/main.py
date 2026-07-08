from customer import Customer
from billing import Billing

customer = Customer()
bill = Billing()

while True:

    print("Menu")
    print("click 1 for adding customer ")
    print("click 2 for view customer ")
    print("click 3 for add vehicle ")
    print("click 4 for view vehicle ")
    print("click 5 for Generate bill ")
    print("click 6 for view bill ")
    print("click 7 for Exit ")
    choice = int(input("Enter Choice: "))

    if choice == 1:
        customer.add_customer()

    elif choice == 2:
        customer.view_customer()

    elif choice == 3:
        customer.add_vehicle()

    elif choice == 4:
        customer.view_vehicle()

    elif choice == 5:
        bill.generate_bill()

    elif choice == 6:
        bill.view_bill()

    elif choice == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")