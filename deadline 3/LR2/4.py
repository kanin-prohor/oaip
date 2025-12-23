def my_range(start, end, step=1):
    current = start
    if step > 0:
        while current < end:
            yield current
            current += step
    elif step < 0:
        while current > end:
            yield current
            current += step

print("Целые числа:")
for num in my_range(1, 5, 1):
    print(num)

print("\nС шагом 0.5:")
for num in my_range(1, 3, 0.5):
    print(num)

print("\nОбратный порядок:")
for num in my_range(5, 1, -1):
    print(num)

print("\nВ список:")
print(list(my_range(0, 1, 0.25)))