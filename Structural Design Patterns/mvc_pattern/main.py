"""
Model View Controller Pattern
-----------------------------
It is a design pattern where the "Separation Of Concerns" principle can be achieved
Functionalities are loosely coupled.
Controller - An endpoint, a URL, an event, action that calls either a view or a Model to feed the view
Model - The business logic, where there is a need to connect to the DB, talk to the file server, cloud storage etc.,
View - Render the data from the model and place it in the appropriate UI components. HTML or React DOM etc.,
"""

from .controllers.GroceryController import GroceryController
from .models.Shop import Grocery

if __name__ == "__main__":
    controller = GroceryController()
    new_item = Grocery(3, "pachai payiru", 500, 50)

    # new grocery item addition
    controller.add_item_controller(new_item)

    # show all grocery items
    controller.get_all_items_controller()

    # udpate grocery item
    new_item.product_name = "vengayam"
    new_item.quantity = 100
    new_item.price = 8

    controller.update_item_controller(new_item)

    # remove grocery item
    controller.remove_item_controller(1)
