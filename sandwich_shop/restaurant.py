"""Module representing a single restaurant entity (player, AI-controlled competition)."""
# import necessary resources
import sandwich
import staff
import menu
import transaction

class Restaurant :
    def __init__(self, name: str, funds: int) :
        self.name = name
        self.funds = funds
        self.staff = [] # initialize empty list for employees
        self.menu = menu.Menu() # initialize empty menu
        self.customers = [] # initialize empty list for customers

    def add_staff(self, name: str, age: int, payrate: int) :
        """Add a staff member to this restaurant's roster."""
        self.staff.append(staff.Employee(name, age, payrate))

    def set_menu(self, menu: menu.Menu):
        """Set a new menu for this restaurant."""
        self.menu = menu

    def add_menu_item(self, sandwich: sandwich.Sandwich) :
        """Add an item to the current menu for the restaurant."""
        self.menu.add_item(sandwich, f'{sandwich=}'.split('=')[0])

    def add_customer(self) :
        """Add a customer to the list of current customers."""
    
    def show_info(self):
        """Display all relevant info about this restaurant instance."""
        print(f'Name: {self.name}\nFunds: {self.funds}\n'
            + f'Employees: {self.staff}\nMenu: {self.menu.get_contents()}'
            + f'Customers present: {self.customers}')

    def run_simulation(self) :
        print("Running..")