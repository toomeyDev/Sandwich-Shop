from random import randint
import json
"""
Control randomly generated events (customer generation, weather etc)
which take place during simulation.
"""
def load_dataset(data_path: str) :
    """
    Open json file at specified path and
    load + return the contents.
    """
    json_file = open(data_path)
    return json.load(json_file)


class Event:
    def __init__(self, event_id: int):
        if event_id == 0:
            # id 0: customer list, a randomly generated list of customers (length = 5 for testing purposes)
            data=load_dataset("resources/actor_values.json")
            self.customers_list = []
            # for i in range(6):
            #     name_selection = randint(0, len(data))
            #     self.customers_list.append(data[])
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