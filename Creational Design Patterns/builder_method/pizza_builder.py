from enum import Enum

pizza_dough = Enum('pizza_dough', 'thin thick')
pizza_sauce = Enum('pizza_sauce', 'marinara bbq')
pizza_toppings = Enum('pizza_toppings', 'bacon jalepeno mozzerella')
STEP_DELAY = 4

class Pizza:
    def __init__(self, builder):
        self.builder = builder
        self.name = builder.name
    
    def prepare_dough(self):
        self.dough = self.builder.dough 
    
    def add_sauce(self):
        self.sauce = self.builder.sauce

    def add_toppings(self):
        self.toppings = self.builder.toppings
    
    def make_pizza(self):
        recipes = (self.prepare_dough, self.add_sauce, self.add_toppings)
        [recipe() for recipe in recipes]
        print()    
        print(f'{self.dough} dough prepared')
        print(f'{self.sauce} sauce added')
        print(f'{self.toppings} toppings added')
        print(f'{self.name} ready')
        print()

class MargaritaPizzaBuilder:
    def __init__(self, name, dough, sauce, toppings):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings

    def make_pizza(self):
        pizza_builder = Pizza(self)
        pizza_builder.make_pizza()


class CrispyCreamyBaconPizzaBuilder:
    def __init__(self, name, dough, sauce, toppings):
        self.name, self.dough, self.sauce, self.toppings = name, dough, sauce, toppings

    def make_pizza(self):
        pizza_builder = Pizza(self)
        pizza_builder.make_pizza()


class Waiter:
    def __init__(self):
        self.builder = None

    def get_pizza(self):
        choice_of_pizza = input('''
        Choose the type of pizza: 
        M - Margarita
        C - Creamy Crispy Bacon
        ?''')
        if choice_of_pizza in 'Mm':
            self.builder = MargaritaPizzaBuilder("Margarita Pizza", pizza_dough.thin.name, pizza_sauce.marinara.name, pizza_toppings.mozzerella.name)
        elif choice_of_pizza in 'Cc':
            self.builder = CrispyCreamyBaconPizzaBuilder("Creamy Crispy Bacon Pizza", pizza_dough.thick.name, pizza_sauce.bbq.name, pizza_toppings.bacon.name)
        else:
            raise("Only (M)Margarita and (C)Creamy Cripy Bacon Pizza available")
        
        self.builder.make_pizza()

def main():
    waiter = Waiter()
    waiter.get_pizza()


if __name__ == "__main__":
    main()