import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        elapsed = end_time - start_time
        print(f"Функция {func.__name__} выполнилась за {elapsed:.6f} секунд")
        
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.5)
    return "Готово!"

@timer
def fast_function():
    return sum(range(1000000))

slow_function()
fast_function()