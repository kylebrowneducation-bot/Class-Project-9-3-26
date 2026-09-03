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
        Initialize all stored data for the object
        """
        pass

    def to_list(self):
        """
        Returns the customer data as a list for CSV file
        """
        pass
    def from_list(self):
        """
        Creates customer object from CSV file
        """
        pass

    def __str__(self):
        """
        Return a string representation of an object
        """
        pass