call_counter = 0

def increment_counter():
    global call_counter
    call_counter += 1

print(f"Начальное значение: {call_counter}")

increment_counter()
print(f"После первого вызова: {call_counter}")

increment_counter()
increment_counter()
print(f"После трёх вызовов: {call_counter}")