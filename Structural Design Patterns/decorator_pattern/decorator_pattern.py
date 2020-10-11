from abc import ABC, abstractmethod


class Coffee(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_ingredients(self):
        pass


class SimpleCoffee(Coffee):
    def get_cost(self):
        return 1

    def get_ingredients(self):
        return "Coffee"

    def __str__(self) -> str:
        return f"Cost: {self.get_cost()}; Ingredients: {self.get_ingredients()}"


class CoffeeDecorator(Coffee):
    def __init__(self, c):
        self._decorated_coffee = c

    def get_cost(self):
        return self._decorated_coffee.get_cost()

    def get_ingredients(self):
        return self._decorated_coffee.get_ingredients()


class WithMilk(CoffeeDecorator):
    def __init__(self, c):
        super().__init__(c)

    def get_cost(self):
        return super().get_cost() + 0.5

    def get_ingredients(self):
        return super().get_ingredients() + ", with Milk"

    def __str__(self) -> str:
        return f"Cost: {self.get_cost()}; Ingredients: {self.get_ingredients()}"


class WithSprinkles(CoffeeDecorator):
    def __init__(self, c):
        super().__init__(c)

    def get_cost(self):
        return super().get_cost() + 0.2

    def get_ingredients(self):
        return super().get_ingredients() + ", with Sprinkles"

    def __str__(self) -> str:
        return f"Cost: {self.get_cost()}; Ingredients: {self.get_ingredients()}"


if __name__ == "__main__":
    sc = SimpleCoffee()
    print(sc)

    wm = WithMilk(sc)
    print(wm)

    ws = WithSprinkles(wm)
    print(ws)
