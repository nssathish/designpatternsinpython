from abc import ABC, abstractmethod

from .Shop import Shop


class _GroceryRepository(ABC):

    @abstractmethod
    def add_item(self, item):
        pass

    @abstractmethod
    def remove_item(self, item_id):
        pass


class GroceryModel(_GroceryRepository):
    def __init__(self):
        shop = Shop().GroceryList()
        self.groceries = shop.groceries

    def add_item(self, item):
        self.groceries.append(item)

    def add_items(self, items):
        [self.add_item(item) for item in items]

    def update_item(self, item_to_update):
        for item in self.groceries:
            if item.product_id == item_to_update.product_id:
                self.remove_item(item_to_update.product_id)
                self.add_item(item_to_update)
                return "Updated"
        else:
            return f"Item id: {item_to_update.product_id} not found"

    def remove_item(self, item_id):
        target_index = 0
        for element in self.groceries:
            if element.product_id == item_id:
                del self.groceries[target_index]

            target_index += 1

    def get_item(self, item_id):
        return [item for item in self.groceries if item.product_id == item_id]
