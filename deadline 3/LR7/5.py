class LoggableMixin:
    def log(self, message: str) -> None:
        class_name = self.__class__.__name__
        print(f"[INFO] {class_name}: {message}")
class Employee(LoggableMixin):
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self._salary = 0.0
        self.salary = salary
    @property
    def salary(self) -> float:
        return self._salary
    @salary.setter
    def salary(self, value: float) -> None:
        if value < 0:
            raise ValueError("Зарплата не может быть отрицательной")
        self._salary = value
class Product(LoggableMixin):
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price
if __name__ == "__main__":
    emp = Employee("Иван", 50000)
    emp.log(f"Создан сотрудник с зарплатой {emp.salary}")
    prod = Product("Ноутбук", 100000)
    prod.log(f"Создан товар по цене {prod.price}")