class Grocery:
    def __init__(self, product_id, product_name, quantity, price):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.price = price


class GroceryList:

    def __init__(self):
        self.groceries = [
            Grocery(1, "ulutham parupu", 500, 100.0),
            Grocery(2, "saamai", 500, 150.0)
        ]


class Shop:
    def __init__(self):
        self.GroceryList = GroceryList
