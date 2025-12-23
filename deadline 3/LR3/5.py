import time

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def tail_fibonacci(n: int, current: int = 0, next_val: int = 1) -> int:
    if n == 0:
        return current
    return tail_fibonacci(n - 1, next_val, current + next_val)

def compare_performance() -> None:
    n = 35
    
    # Обычная рекурсия
    start = time.perf_counter()
    fib_normal = fibonacci(n)
    time_normal = time.perf_counter() - start
    
    # Хвостовая рекурсия
    start = time.perf_counter()
    fib_tail = tail_fibonacci(n)
    time_tail = time.perf_counter() - start
    
    print(f"fibonacci({n}) = {fib_normal}, время: {time_normal:.4f} сек")
    print(f"tail_fibonacci({n}) = {fib_tail}, время: {time_tail:.6f} сек")
    print(f"Хвостовая рекурсия быстрее в {time_normal/time_tail:.0f} раз")

if __name__ == "__main__":
    compare_performance()