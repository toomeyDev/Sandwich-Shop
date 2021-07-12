class Sandwich :
    def __init__(self, bread='white', portion=1,*ingredients):
        self.bread = bread
        self.portion = portion
        self.type = 'sandwich'
        self.ingredients = [] # hold any ingredients (meat, mustard, etc)
        for ingredient in ingredients:
            # add each ingredient specified to the list of ingredients for the sandwich
            ingredients.append(ingredient)

class Sub(Sandwich):
    def __init__(self, bread='white', length=6, toasted = False, *ingredients):
        super().__init__() # call parent class constructor for access to default/basic values for a sandwich
        self.bread = bread
        self.length = length
        self.type = 'sub'
        self.toasted = toasted
        for ingredient in ingredients:
            # add each ingredient provided to list of ingredients for this sub
            ingredients.append(ingredient)

class Burger(Sandwich) :
    def __init__(self, bread='white', portion=1, temp='medium-rare', fat_percentage='2%', *ingredients):
        super().__init__() # call parent class constructor for access to basic values from parent class
        self.bread = bread
        self.portion = portion
        self.temp = temp
        self.fat_percentage = fat_percentage
        for ingredient in ingredients:
            # add each provided ingredient to list of ingredients for this burger
            ingredients.append(ingredient)