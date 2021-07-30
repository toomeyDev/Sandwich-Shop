"""
Contains classes & functions related to funding, finances, transactions,
should handle all movement of money within the program.
"""

class Wallet:
    """Initialize this wallet with provided values or defaults."""
    def __init__(self, initial_funding: float=0, owner: str='default'):
        self.balance = initial_funding
        self.owner = owner #current owner of this wallet

    def get_balance(self):
        """Return the current balance of this wallet, rounded to two decimal pts."""
        return round(self.balance, 2)

    def change_balance(self, amount, overwrite=True):
        """
        Modify the balance of this wallet object, either overwrites with
        provided value (default) or adds the provided values to the balance
        (overwrite=False).
        """
        if overwrite:
            self.balance = amount
        else:
            self.balance += amount        

    def format_balance(self) -> str:
        """Format and return current balance in easily legible format."""
        return(f"{self.owner}'s current balance: {self.balance}")


def transaction(source: Wallet, destination: Wallet, amt: float):
    """
    Handle transactions between two balances (customer->restauraunt),
    (restaurant->bills) etc.
    """
    source.balance -= amt
    destination.balance += amt

    