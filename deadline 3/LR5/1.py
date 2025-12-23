class Student:
    def __init__(self, name: str, average_score: float) -> None:
        self.name = name
        self.average_score = average_score
    
    def is_excellent(self) -> bool:
        return self.average_score == 5