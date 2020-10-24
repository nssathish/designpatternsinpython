from ..models.GroceryModel import GroceryModel
from ..views.GroceryView import GroceryView


class GroceryController:

    def __init__(self):
        self.GroceryModel = GroceryModel()
        self.GroceryView = GroceryView()

    # (C)RUD - Create
    def add_items_controller(self, grocery_items):
        self.GroceryModel.add_items(grocery_items)

    def add_item_controller(self, grocery_item):
        self.GroceryModel.add_item(grocery_item)

    # C(R)UD - Read
    def get_all_items_controller(self):
        groceries = self.GroceryModel.groceries
        self.GroceryView.show_items(groceries)

    def get_item_controller(self, item_id):
        groceries = self.GroceryModel.groceries
        self.GroceryView.show_item(groceries, item_id)

    # CR(U)D - Update
    def update_item_controller(self, item):
        self.GroceryModel.update_item(item)
        self.GroceryView.show_items(self.GroceryModel.groceries)

    # CRU(D) - Delete
    def remove_item_controller(self, item_id):
        self.GroceryModel.remove_item(item_id)
        self.GroceryView.show_items(self.GroceryModel.groceries)
