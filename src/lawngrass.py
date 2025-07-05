from src.product import Product


class LawnGrass(Product):
    """Класс-наследник класса Product - класс «Трава газонная»"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Метод для ограничения сложения разных классов."""
        if type(other) is self.__class__:
            return self.quantity + other.quantity
        raise TypeError
