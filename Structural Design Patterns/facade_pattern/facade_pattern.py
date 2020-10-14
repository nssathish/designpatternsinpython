"""
Facade pattern
---------------
A pattern which creates a simple entry points for complex implementations in the system
This brings in loosely coupled modules for ease of changes and no change to the client facing interfaces
Testable code

Use case
--------
1. The pattern is used to when there is a need to create simple entry points for the complex system
2. When we want to provide a unique structure to a subsystem by dividing them into layers
3. When there is need for loose coupling between client and the subsystem
"""

from abc import ABC, abstractmethod
from enum import Enum

VegMenu = Enum('VegMenu', 'idli dosai vadai')
NonVegMenu = Enum('NonVegMenu', 'chicken mutton lobster')


class Hotel(ABC):

    @abstractmethod
    def get_menus(self):
        pass


class VegHotel(Hotel):

    def __init__(self) -> None:
        self.menus = None

    def get_menus(self):
        self.menus = list({"vadai", "dosai", "idli"})
        return self


class NonVegHotel(Hotel):

    def __init__(self) -> None:
        self.menus = None

    def get_menus(self):
        self.menus = list({"chicken", "mutton", "pomfret"})
        return self


class MultiCuisine(Hotel):

    def __init__(self) -> None:
        self.menus = None

    def get_menus(self):
        veg_hotel = VegHotel().get_menus()
        non_veg_hotel = NonVegHotel().get_menus()
        self.menus = list()
        self.menus.append(veg_hotel.menus)
        self.menus.append(non_veg_hotel.menus)

        return self


class HotelKeeper:

    def __init__(self) -> None:
        self.veg_hotel_obj = VegHotel()
        self.non_veg_hotel_obj = NonVegHotel()
        self.multicuisine_obj = MultiCuisine()

    def get_veg_menu(self):
        return self.veg_hotel_obj.get_menus().menus

    def get_non_veg_menu(self):
        return self.non_veg_hotel_obj.get_menus().menus

    def get_multicuisine_menu(self):
        return self.multicuisine_obj.get_menus().menus


if __name__ == "__main__":
    keeper = HotelKeeper()
    veg_menus = keeper.get_veg_menu()
    non_veg_menus = keeper.get_non_veg_menu()
    multicuisine_menus = keeper.get_multicuisine_menu()

    print(veg_menus, non_veg_menus, multicuisine_menus)
