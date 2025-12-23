from dataclasses import dataclass, field

@dataclass(frozen=True, repr=False)
class Product:
    name: str
    price: float
    weight: float
    is_available: bool = True
    def __repr__(self) -> str:
        return f"Product(name='{self.name}', weight={self.weight}, is_available={self.is_available})"
    def order_cost(self, quantity: int) -> float:
        return self.price * quantity