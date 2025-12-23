def simple_calculator(a, b, op):
    return {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b if b != 0 else "Ошибка"
    }.get(op, "Неизвестная операция")