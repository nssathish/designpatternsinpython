class GroceryView:

    def __init__(self):
        self.groceries = None

    def show_items(self, grocery_list):
        if self.groceries is None:
            self.groceries = grocery_list
        print(f'Items in the store: {len(self.groceries)}')

        for item in self.groceries:
            print(item)
            print(f"""
                product id: {item.product_id}
                product name: {item.product_name}
                quantity: {item.quantity}
                price: {item.price}
            """)

    def show_item(self, grocery_list, item_id):
        if self.groceries is None:
            self.groceries = grocery_list

        print(f'Items in the store: {len(self.groceries)}')
        items = [item for item in self.groceries if item.product_id == item_id]
        [print(f"""
                product id: {item.product_id}
                product name: {item.product_name}
                quantity: {item.quantity}
                price: {item.price}
            """) for item in items]
