"""
Proxy Pattern
-------------
A proxy pattern is a class acting as an interface to another class.
A proxy can interface to anything
    1. a network connection
    2. a large object in memory
    3. a file
that are expensive or impossible to duplicate

Use-Cases
---------
1. Use of the proxy can be simply forward to the real object (with or without additional logic)

Types
-----
1. Remote Proxy - in Distributed Object Communication - a local object can refer a remote method and invoking that
                    object will do the remote method invocation. Eg., ATM implementation - where the ATM holds the
                    proxy objects for bank information that exists in the remote server
2. Virtual Proxy (look at lazy loading: https://en.wikipedia.org/wiki/Lazy_loading) - if the object is
                    heavy/complicated - a skeleton of the representation is better - it may be represented using a
                    virtual proxy object and the real object can be invoked on demand
3. Protection Proxy - a protection proxy might be used to control access to a resource based on access rights
"""

from abc import ABC, abstractmethod


class ICar(ABC):
    @abstractmethod
    def drive(self):
        raise NotImplementedError('You have to implement this')


class Driver:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return self.name


class Car(ICar):

    def __init__(self, driver: Driver):
        self.driver = driver

    def drive(self):
        print(f'{self.driver} can drive the car')


class ProxyCar(ICar):

    def __init__(self, driver: Driver) -> None:
        self.driver = driver

    def drive(self):
        if self.driver.age < 16:
            print(f'{self.driver} under aged (age: {self.driver.age}) to drive.')
        else:
            car = Car(self.driver)
            car.drive()


if __name__ == "__main__":
    driver = Driver('sathish',33)
    celerio = Car(driver)
    celerio.drive()

    fortuner = ProxyCar(driver)
    fortuner.drive()
