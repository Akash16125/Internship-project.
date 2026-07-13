from database import Database

class Admin:
    def __init__(self):
        self.db=Database()
    
    def login(self):
        username=input("ENTER USERNAME: ")
        password=input("ENTER PASSWORD: ")
        query="SELECT * FROM admin WHERE username=%s AND password=%s"

        self.db.execute(query,(username,password))

        admin=self.db.fetchone()

        if admin:
            print("ADMIN LOGIN SUCCESSFULLY.....")
            self.dashboard()
        else:
            print("INVALID ADMIN CREDENTIALS")

    def view_all_users(self):

        query="""SELECT id,name,email,mobile,username,created_at FROM users"""

        self.db.execute(query)
        users=self.db.fetchall()

        if not users:
            print("NO USER FOUND")
            return
        
        print("\n============================== USERS ===========================================")

        for user in users:
            print(f"""
ID         : {user[0]}
NAME       : {user[1]}
EMAIL      : {user[2]}
MOBILE     : {user[3]}
USERNAME   : {user[4]}
CREATED AT : {user[5]}         
------------------------------------------------------------------------------   
""")
            
    def search_user(self):
        username = input("ENTER USERNAME: ")
        query=""""SELECT id,name,email,mobile,username,created_at FROM users WHERE username=%s"""
        
        self.db.execute(query, (username,))
        user=self.db.fetchone()

        if user:
            print(f"""
ID         : {user[0]}
NAME       : {user[1]}
EMAIL      : {user[2]}
MOBILE     : {user[3]}
USERNAME   : {user[4]}
CREATED AT : {user[5]}         
------------------------------------------------------------------------------   
""")
        else:
            print("USER NOT FOUND")

    def delete_user(self):
        username = input("ENTER USERNAME: ")
        query=""""SELECT * FROM users WHERE username=%s"""

        self.db.execute(query, (username,))
        user=self.db.fetchone()

        if not user:
            print("USER NOT FOUND")
            return
        choice=input("DELETE USER (Y/N): ")

        if choice.lower()=="y":
            query="DELETE FROM users WHERE username=%s"

            self.db.execute(query, (username,))
            
            print("User Deleted Successfully")

        else:
            print("Cancelled")

    
    def total_user(self):

        query="SELECT COUNT(*) FROM users"

        self.db.execute(query)
        total=self.db.fetchone()

        print("Total Users: ",total[0])

    def dashboard(self):

        while True:
            print("\n============== ADMIN DASHBOARD ===================")
            print("1. View All Users")
            print("2. Search Users")
            print("3. Delete Users")
            print("4. Total Users")
            print("5. Logout")

            choice =int(input("\n SELECT SERVICE: "))
            if choice==1:
                self.view_all_users()
            elif choice==2:
                self.search_user()
           
            elif choice==3:
                self.delete_user()
           
            elif choice==4:
                self.total_user()
           
            elif choice==5:
                print("Admin Logout Successfully")
                break

            else:
                print("Invalid Choice")