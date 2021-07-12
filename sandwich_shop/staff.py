class Employee :
    """Represents one single employee with name, gender, age, and payrate attributes."""
    def __init__(self, name, age, pay_rate):
        self.name = name
        self.age = age
        self.pay_rate = pay_rate
    
    def display_info(self):
        """Display all attributes of the employee."""
        print(f"Employee Info: {self.name}, age {self.age}, payrate: {self.pay_rate}")