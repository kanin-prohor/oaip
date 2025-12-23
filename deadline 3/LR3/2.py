def sum_digits(number: int) -> int:
    if abs(number) < 10:
        return abs(number)
    return abs(number) % 10 + sum_digits(abs(number) // 10)