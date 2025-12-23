def power(a: float, n: int) -> float:
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(a, -n)
    if n % 2 == 0:
        half = power(a, n // 2)
        return half * half
    return a * power(a, n - 1)