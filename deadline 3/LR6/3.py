class Multiplier:
    def __init__(self, multiplier: float) -> None:
        self.multiplier = multiplier
    def __call__(self, number: float) -> float:
        return self.multiplier * number