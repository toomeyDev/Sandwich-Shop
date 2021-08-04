import sandwich
from finance import Wallet
from finance import transaction
"""
Contains classes related to "human" characters within the simulation (employees, customers).
"""

"""Represents a single customer with a name, list of sandwiches to order."""
class Customer:
    """Initialize customer with provided arguments, or use defaults."""
    def __init__(self, name: str='default', order: list[sandwich.Sandwich]=[], balance=0):
        self.name = name
        self.order = order
        self.balance = Wallet(balance, self.name)
    
    def order_food(self, destination_wallet: Wallet):
        """Attempt to order the items on this customer's order list."""
        # get total $ amt of order for transaction
        order_total = 0
        for item in self.order:
            order_total += item.price
        
        if self.balance.get_balance() >= order_total:
            transaction(self.balance, destination_wallet, order_total)
            print(f"{self.name} has paid {order_total} for their order, and now has {self.balance.get_balance()} left over.")
        else:
            print(f"{self.name} cannot afford this order!")

"""Represents a single employee with a specific job title."""
class Employee:
    """Initialize employee with provided arguments, or use defaults."""
    def __init__(self, name='default', position='base', pay_rate=50.00):
        self.name = name
        self.position = position
        self.pay_rate=pay_rate # payrate of this employee, should be subtracted from restauraunt funds at end of shift