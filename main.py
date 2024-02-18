class User:

    # class parameters
    def __init__(self):
        # Initialize instance attributes
        self.__username = ""
        self.__password = ""
        self.__firstName = ""
        self.__lastName = ""
        self.__email = ""
        self.__contact = ""
        self.__dateOfBirth = ""
        self.__gender = ""
        self.__address = ""
        self.__userID = 0

    # Setters
    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def set_firstName(self, firstName):
        self.__firstName = firstName

    def set_lastName(self, lastName):
        self.__lastName = lastName

    def set_email(self, email):
        self.__email = email

    def set_contact(self, contact):
        self.__contact = contact

    def set_dateOfBirth(self, dateOfBirth):
        self.__dateOfBirth = dateOfBirth

    def set_gender(self, gender):
        self.__gender = gender

    def set_address(self, address):
        self.__address = address

    def set_userID(self, userID):
        self.__userID = userID

    # Getters
    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_firstName(self):
        return self.__firstName

    def get_lastName(self):
        return self.__lastName

    def get_email(self):
        return self.__email

    def get_contact(self):
        return self.__contact

    def get_dateOfBirth(self):
        return self.__dateOfBirth

    def get_gender(self):
        return self.__gender

    def get_address(self):
        return self.__address

    def get_userID(self):
        return self.__userID


# Usage
u = User()
u.set_username("Ralf")
print(u.get_username())  # Output: Ralf
