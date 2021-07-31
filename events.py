"""
Control randomly generated events (customer generation, weather etc)
which take place during simulation.
"""

class Event:
    def __init__(self, event_id: int):
        if event_id == 0:
            # id 0: customer list, a randomly generated list of customers (length = 5 for testing purposes)
            self.customers_list = []
        elif event_id == 1:
            # id 1: weather, randomly generated weather event which lasts the entire day
            self.weather = '' # placeholder, pending weather logic implementation

def day_start():
    """
    Start a day of customers, weather etc for the user restauarant.
    """

def day_end():
    """
    End a day for final profit/loss calculation and inventory calculation.
    """