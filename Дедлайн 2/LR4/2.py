import random
numbers = [random.randint(1, 100) for _ in range(10)]
print(f"Исходный список: {numbers}")
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"Четные числа: {even_numbers}")
gt_50 = [x for x in numbers if x > 50]
print(f"Числа > 50: {gt_50}")