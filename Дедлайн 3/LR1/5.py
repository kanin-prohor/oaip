def safe_exec(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль!")
            return 0
    return wrapper

@safe_exec
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(5, 0))

@safe_exec
def complex_calculation(x, y):
    return (x + y) / (x - y)

print(complex_calculation(10, 5))
print(complex_calculation(5, 5))