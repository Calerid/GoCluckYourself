class Customer:
    """Represents an individual customer within the application"""
    def __init__(self, customer_id, name, phone, notes):
        """
        Customer:

        
        """
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.notes = notes

class Sale:
    """Represents a sale object within the application."""
    def __init__(self, transaction_id, date, amount, quantity):
        """
        Sale: 
        Represents an individual sale within the application and database.
        Each sale will contain the id, date, amount, and quantity of eggs.
        If a sale is deleted, all sales proceeding will be decremented by one.
        The quantity, and amount should be the only alterable values.

        Parameters:
        param transaction_id (int): Unique identifier for an individual sale.
        param date (str): Accepts a string value MM:DD:YYYY
        param amount (float): Acecpts a floating point value for the amount of a sale.
        param quantity (int): Accepts an integer for the amount of eggs sold.
        """
        self.transaction_id = transaction_id
        self.date = date
        self.amount = amount
        self.quantity = quantity

        def create(self, transaction_id, date, amount, quantity):
            

        def delete(self, transaction_id):       


        def update_amount(self, transaction_id, amount):


        def update_quantity(self, transaction_id, quantity):

     

class Chicken:
    """Represents an individual chicken object in the application"""
    def __init__(self, chicken_id, name, breed, birth, cost, death, status, sale_price):
        """
        Chicken:
        Represents an individual chicken in the database. The name, status, and death 
        param chicken_id (int): Unique identifier for a chicken object.
        param name (str): Accepts a string value and has a method for updating.
        param breed (str): Accepts a string value for defining the breed.
        param birth (str): Accepts a string value MM:DD:YYYY
        param cost (float): Accepts a floating point value for the total cost of a chicken.
        param death (str): Accepts a string value MM:DD:YYYY.
        param status (str): Accepts an string either active, sold, or deceased.
        """
        self.chicken_id = chicken_id
        self.name = name
        self.breed = breed
        self.birth = birth
        self.cost = cost
        self.death = death
        self.status = status
        self.sale_price = sale_price




