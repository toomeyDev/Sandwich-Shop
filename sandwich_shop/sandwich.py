class Sandwich:
    def __init__(self, type='sandwich', bread='white', price = 0.00, *args):
        """
        Initialize this sandwich with provided type, bread, fillings
        """
        self.type = type #type of sandwich, ie sandwich, hot-dog, taco
        self.bread = bread #type of bread, ie wheat, rye, corn tortilla
        self.price = price #price of sandwich
        self.fillings = []
        #add all specified fillings to fillings list
        for filling in args:
            self.fillings.append(filling)


    def set_price(self, price):
        """Set the price of this sandwich, overwriting previous price."""
        if(price > 0):
            self.price = price
        else:
            print("Price must be greater than 0.")

    def fillings_to_string(self):
        """Convert all fillings present in this sandwich to string format."""
        fillings_string = ''
        for filling in self.fillings:
            fillings_string += f"{filling}, "
        return fillings_string


    def print_sandwich_details(self):
        """Print details of this sandwich to console."""
        print(f"This is a {self.type}, with {self.fillings_to_string()}on {self.bread}.")
        print(f"Price is {self.price}.")