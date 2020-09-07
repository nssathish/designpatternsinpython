"""
    The abstract factory pattern
    ----------------------------
    1.A group of factory methods where each factory method is responsible for generating
    a different kind of object.

    Real-world eg.,
    ---------------
    1. Car manufacturing. Same machinery is used for stamping the parts, doors, panels,
    hoods, fenders, mirrors etc., of different car models
    2. 'factory_boy' in Django provides an abstract factory implementation for creating
    models in tests. 

    Use cases
    ---------
    1. When the object creation cannot be managed by the application because the object gets
    created in multiple places rather than in a single place/method.
    2. When we want to decouple of object creation from object usage. 
    3. To improve the performance and memory usage of the application since the objects are
    created only on demand

    When to use abstract-factory and factory pattern
    ------------------------------------------------
    Start with factory method, if we find out our application requires many factory methods
    which it makes sense to create a family of objects, we end up with an abstract factory

    A benefit of abstract factory that is usually not very visible from a user's point of 
    view is that it helps the application to determine the factory method at runtime. 

    Eg., The change in the look and feel of the application in Mac (Apple-like), PC (windows-like)
    dynamically at runtime

    Example here
    ------------
    a game for kids and adults. Abstract factory takes care of game creation
"""
class Frog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'{self} the frog encounters {obstacle} and {act}'
        print(msg)


class Bug:
    def __str__(self):
        return 'a bug'
    
    def action(self):
        return 'eat it'


class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------------ Frog World ---------'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class Wizard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'{self} the wizard battles against the {obstacle} and {act}'
        print(msg)


class Ork:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def action(self):
        return "kills it"


class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t--------- Wizard world -------'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork(" an evil ork ")


class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()
    
    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    try:
        age = input(f'Welcome {name}. How old are you? ')
        age = int(age)
    except ValueError:
        print(f"Age {age} is invalid, please try again...")
        return (False, age)
    return (True, age)


def main():
    name = input("Hello. What's your name? ")
    valid_input = False
    age = None
    while not valid_input:
        valid_input, age = validate_age(name)

    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()


if __name__ == "__main__":
    main()