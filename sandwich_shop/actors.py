import sandwich
"""
Contains classes related to "human" characters within the simulation (employees, customers).
"""

"""Represents a single customer with a name, list of sandwiches to order."""
class Customer:
    """Initialize customer with provided arguments, or use defaults."""
    def __init__(self, name: str='default', order: list[sandwich.Sandwich]=[]):
        self.name = name
        self.order = order

"""Represents a single employee with a specific job title."""
class Employee:
    """Initialize employee with provided arguments, or use defaults."""
    def __init__(self, name='default', position='base'):
        self.name = name
        self.position = position