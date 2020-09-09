"""
    The builder pattern
    -------------------
    1. When the object creation has multiple parts and the composition needs to be done
    step by step.
    2. The object is created only when all the parts are compeleted
    3. It separates the construction of the complext object from representation.

    Components
    ----------
    The Builder: The component responsible for creating the various parts of a
    complex object.
    The Director: The component that controls the building process using a builder 
    instance calling all the builder methods

    Real-world eg.,
    ---------------
    1. Food Restaurants. Same building process is always used to prepare a burger even 
    if there are many different kinds of burgers and packaging
        a. 'director': the cashier who gives instructions on what needs to be prepared
        b. 'builder': the person from the crew to takes care of the specific order
    2. Content Management System (CMS): To create HTML pages with different layouts
    3. Django-Querybuilder lib: building SQL queries dynamically

    Use cases
    ---------
    1. When the object must be created in multiple steps and different representations of
    the same construction is required.
    2. When the object creation cannot be managed by the application because the object gets
    created in multiple places rather than in a single place/method.

    When to use Builder Pattern
    ---------------------------
    With *One Construction* multiple representations of the object can be created
    Eg., HTML page generator, document converter ('convert' operation for different documents)
    "Telescopic constructor problem"

    Unlike the factory pattern (creates an object in a single step and immediately), in the
    builder pattern the client will ask for the final object to be released by the "director"

    Example here
    ------------
    a game for kids and adults. Abstract factory takes care of game creation
"""

class AppleFactory:
    class Mini14:
        def __init__(self):
            self.hdd = '256'
            self.ram = '8'
            self.cpu = 'Intel Core i5'
            self.size = '14'

        def __str__(self):
            return f"""
            Built Apple Mac Mini {self.size}
            Hard disk: {self.hdd} GB
            Ram: {self.ram} GB
            CPU: {self.cpu}
            """
    
    def build_computer(self, model):
        if model == 'Mini14':
            return self.Mini14()
        else:
            return f"I don't know how to build the {model}"


if __name__ == "__main__":
    factory = AppleFactory()
    mini14 = factory.build_computer(input('Mac model?: '))
    print(mini14)