def logger(func):
    def wrapper(*args, **kwargs):
        args_str = ', '.join(map(repr, args))
        kwargs_str = ', '.join(f'{k}={repr(v)}' for k, v in kwargs.items())
        all_args = ', '.join(filter(None, [args_str, kwargs_str]))
        
        print(f"Вызов функции {func.__name__} с аргументами: {all_args}")
        
        result = func(*args, **kwargs)
        
        print(f"Результат: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

@logger
def greet(name, age=None):
    if age:
        return f"Привет, {name}! Тебе {age} лет."
    return f"Привет, {name}!"

add(5, 3)
greet("Анна", age=25)