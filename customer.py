# The customer class should be able to store the following:


# -Name
# -Address
# -City, State, Zip
# -Telephone Number
# -Account Balance
# -Date of Last Payment

class Customer:

    def __init__(self):
        """
        Initializing all stored data for the object
        """
        self.name = ""
        self.address = ""
        self.city = ""
        self.state = ""
        self.zip = ""
        self.telephone = ""
        self.account_balance = 0.0
        self.date_last_payment = ""

    def to_list(self):
        """
        Returns the customer data as a list for CSV file
        """
        return [
            self.name,
            self.address,
            self.city,
            self.state,
            self.zip,
            self.telephone,
            self.account_balance,
            self.date_last_payment
        ]

    def from_list(self, data):
        """
        Creates customer object from CSV file
        """
        self.name = data[0]
        self.address = data[1]
        self.city = data[2]
        self.state = data[3]
        self.zip = data[4]
        self.telephone = data[5]
        self.account_balance = float(data[6])
        self.date_last_payment = data[7]

    def __str__(self):
        """
        Return a string representation of an object
        """
        return (
            f"Name: {self.name}\n"
            f"Address: {self.address}\n"
            f"City: {self.city}\n"
            f"State: {self.state}\n"
            f"Zip: {self.zip}\n"
            f"Telephone Number: {self.telephone}\n"
            f"Account Balance: ${self.account_balance:.2f}\n"
            f"Date of Last Payment: {self.date_last_payment}"
        )