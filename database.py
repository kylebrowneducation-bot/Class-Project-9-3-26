# The customer class should also be able to store its data in a comma separated value (.csv) file.   
# The class should have the capability to load from the file upon initialization and update the file on command/when the program exits.    
# There should also be commands on performing basic operations.  

class CustomerDatabase:

    def __init__(self):
        pass

    def load(self):
        """
        Loads csv data
        """
        pass

    def save(self):
        """
        Saves all customer data to the CSV
        """
        pass

    def update_name(self, customer):
        """
        Changes customer name
        """
        pass

    def update_address(self, customer):
        """
        Changes customer address
        """
        pass

    def update_location(self, customer):
        """
        Changes city, state, zip
        """
        pass
    
    def update_phonenumber(self, customer):
        """
        Changes customer phone number
        """
        pass

    def update_balance(self, customer):
        """
        Updates customer balance
        """
        pass
    def update_payment(self, customer):
        """
        Updates customer last payment
        """
        pass

    def delete(self, customer):
        """
        Remove a customer from the CSV
        """
        pass

    def add_customer(self, customer):
        """
        Add a customer to the CSV
        """
        pass

    def reset_database(self):
        """
        Resets the CSV
        """
        pass

    def find_customer(self, name):
        """
        Locates a customer in the CSV
        """
        pass

    def list_all(self):
        """
        Returns all rows in CSV
        """
        pass

