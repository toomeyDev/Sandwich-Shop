"""
Contains classes & functions related to funding, finances, transactions,
should handle all movement of money within the program.
"""

class Wallet:
    """Initialize this wallet with provided values or defaults."""
    def __init__(self, initial_funding: float =0, owner: str = 'default'):
        self.balance = initial_funding
        self.owner = owner #current owner of this wallet

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
    print(source.format_balance()) # temporary, remove once simulation is at minimum functionality
    print(destination.format_balance()) # see above

    