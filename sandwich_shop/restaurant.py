"""Module representing a single restaurant entity (player, AI-controlled competition)."""
# import necessary resources
import sandwich
import staff
import transaction

class Restaurant:
    def __init__(self, name: str, funds: int):
        self.name = name
        self.funds = funds
        self.staff = [] # initialize empty list for employees
        self.menu = [] # initialize empty list for menu