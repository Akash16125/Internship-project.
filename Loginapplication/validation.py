import re


class Validation:

  
    def is_empty(self, value):

        if value.strip() == "":
            return False

        return True


  
    def validate_name(self, name):

        if len(name) < 3:
            return False

        if not name.replace(" ", "").isalpha():
            return False

        return True


    def validate_email(self, email):

        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if re.match(pattern, email):
            return True

        return False


    def validate_mobile(self, mobile):

        if len(mobile) != 10:
            return False

        if not mobile.isdigit():
            return False

        return True


    def validate_username(self, username):

        if len(username) < 4:
            return False

        return True


    def validate_password(self, password):

        if len(password) < 8:
            return False

        upper = False
        lower = False
        digit = False
        special = False

        special_char = "!@#$%^&*()_+-="

        for ch in password:

            if ch.isupper():
                upper = True

            elif ch.islower():
                lower = True

            elif ch.isdigit():
                digit = True

            elif ch in special_char:
                special = True

        if upper and lower and digit and special:
            return True

        return False


 
    def confirm_password(self, password, confirm):

        return password == confirm