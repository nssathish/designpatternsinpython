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

class Computer:
    def __init__(self, name):
        self.name = name
        self.hdd = 0
        self.ram = 0
        self.cpu = ""
        self.size = 0

    def __str__(self):
        return f"""
        Built the PC: {self.name}
        Hard disk: {self.hdd} GB
        RAM: {self.ram} GB
        CPU: {self.cpu}
        Size: {self.size} Inches
        """


class ComputerBuilder:
    def __init__(self, name):
        self.computer = Computer(name)

    def configure_memory(self, hdd):
        self.computer.hdd = hdd
    
    def configure_ram(self, ram):
        self.computer.ram = ram

    def configure_cpu(self, cpu):
        self.computer.cpu = cpu

    def configure_size(self, size):
        self.computer.size = size


class HardwareEngineer:
    def __init__(self):        
        self.builder = None
    
    def construct_computer(self, name, hdd, ram, cpu, size):
        self.builder = ComputerBuilder(name)
        steps = (
            self.builder.configure_memory(hdd),
            self.builder.configure_ram(ram),
            self.builder.configure_cpu(cpu),
            self.builder.configure_size(size)
        )

        [step for step in steps]

    @property
    def computer(self):
        return self.builder.computer


def main():
    engineer = HardwareEngineer()
    engineer.construct_computer("PC1235", 256, 8, "Intel Core i7 chipset", 15)
    computer = engineer.computer
    print(computer)


if __name__ == "__main__":
    main()