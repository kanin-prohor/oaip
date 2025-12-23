class Employee:
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