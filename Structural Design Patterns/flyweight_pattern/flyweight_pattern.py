"""
Flyweight Pattern
-----------------
It is a optimization design pattern.
Optimization - improved performance and memory usage
    1. Data Sharing between similar objects
    2. Flyweight is a shared object that contains
        a. state-independent immutable (known as intrinsic) data
        b. If flyweight needs "state-dependent, mutable (extrinsic) data"
        then it should be provided to it by the client code
    3. Implementation definitions of similar properties should be grouped (classified)

Use Cases
---------
It's all about improving performance and memory usage.
All embedded systems
    a. Phones, tablets, games consoles, microcontrollers etc.,
performance critical applications
    a. Games, 3-D graphics processing, real-time systems etc.,

Requirements to identify the need of the flyweight pattern
----------------------------------------------------------
1. There are requirements to create large number of objects
2. Creating large number of object and maintaining it is hard.
3. Objects' identity does not matter.

"""
from enum import Enum
import random


CarTypes = Enum('CarTypes', 'subcompact compact suv')


class Car:
    pool = dict()

    def __new__(cls, car_type) -> object:
        car_type_obj = Car.pool.get(car_type, None)
        if not car_type_obj:
            car_type_obj = object.__new__(cls)
            Car.pool[car_type] = car_type_obj
            cls.car_type = car_type
        return car_type_obj

    def render(self, color, x, y) -> str:
        model = self.car_type
        return f'render {model} car in {color} at location ({x}, {y})'


def main():
    rnd = random.Random()
    colors = ['red', 'blue', 'green', 'violet', 'black', 'white']
    min_coordinate, max_coordinate = 0, 100
    car_counter = 0

    for _ in range(10):
        c1 = Car(CarTypes.subcompact)
        c1.render(random.choice(colors), rnd.randint(min_coordinate, max_coordinate), rnd.randint(min_coordinate, max_coordinate))
        car_counter += 1

    for _ in range(5):
        c2 = Car(CarTypes.compact)
        c2.render(random.choice(colors), rnd.randint(min_coordinate, max_coordinate), rnd.randint(min_coordinate, max_coordinate))
        car_counter += 1

    for _ in range(3):
        c3 = Car(CarTypes.suv)
        c3.render(random.choice(colors), rnd.randint(min_coordinate, max_coordinate), rnd.randint(min_coordinate, max_coordinate))
        car_counter += 1

    c4 = Car(CarTypes.subcompact)
    c5 = Car(CarTypes.subcompact)
    c6 = Car(CarTypes.suv)

    print(f'Cars rendered: {car_counter}')
    print(f'Cars actually created: {len(Car.pool)}')

    print(f'{id(c4)} == {id(c5)} ? {id(c4) == id(c5)}')
    print(f'{id(c5)} == {id(c6)} ? {id(c5) == id(c6)}')


if __name__ == "__main__":
    main()
