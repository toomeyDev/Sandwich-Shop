class Sandwich :
    def __init__(self, bread='white', portion=1,*ingredients):
        self.bread = bread
        self.portion = portion
        self.type = 'sandwich'
        self.ingredients = [] # hold any ingredients (meat, mustard, etc)
        for ingredient in ingredients:
            # add each ingredient specified to the list of ingredients for the sandwich
            self.ingredients.append(ingredient)
    
    def display_info(self):
        """Display info related to a particular sandwich."""
        print(f" Bread: {self.bread}\n Portion: {self.portion}\n Type: {self.type}\n Ingredients: {self.ingredients}")

class Sub(Sandwich):
    def __init__(self, bread='white', length=6, toasted = False, *ingredients):
        super().__init__() # call parent class constructor for access to default/basic values for a sandwich
        self.bread = bread
        self.length = length
        self.type = 'sub'
        self.toasted = toasted
        for ingredient in ingredients:
            # add each ingredient provided to list of ingredients for this sub
            self.ingredients.append(ingredient)

    def display_info(self):
        """Display info related to a particular sub."""
        print(f" Bread: {self.bread}\n Length: {self.length}\"\n Type: {self.type}\n Toasted: {self.toasted}\n Ingredients: {self.ingredients}")

class Burger(Sandwich) :
    def __init__(self, bread='white', portion=1, temp='medium-rare', fat_percentage='2%', *ingredients):
        super().__init__() # call parent class constructor for access to basic values from parent class
        self.bread = bread
        self.portion = portion
        self.temp = temp
        self.fat_percentage = fat_percentage
        for ingredient in ingredients:
            # add each provided ingredient to list of ingredients for this burger
            self.ingredients.append(ingredient)
        
    def display_info(self):
        """Display info related to a particular burger."""
        print(f" Bread: {self.bread}\n Portion: {self.portion}\n" 
        + f" Type: {self.type}\n Doneness: {self.temp}\n" 
        + f" Fat-Content: {self.fat_percentage}\n Ingredients: {self.ingredients}")