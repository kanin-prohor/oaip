class StringUtils:
    @staticmethod
    def invert(string: str) -> str:
        return string[::-1]
    @staticmethod
    def normalize(string: str) -> str:
        return string.strip().lower()
class User:
    def __init__(self, name: str, role: str) -> None:
        self.name = name
        self.role = role
    @classmethod
    def from_string(cls, data_string: str) -> 'User':
        parts = [part.strip() for part in data_string.split(';')]
        if len(parts) != 2:
            raise ValueError("Строка должна быть в формате 'Name;Role'")
        return cls(parts[0], parts[1])