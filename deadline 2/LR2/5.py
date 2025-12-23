n = int(input("Количество чисел: "))
nums = []
i = 0
while i < n:
    nums.append(float(input(f"Число {i+1}: ")))
    i += 1
max_num = nums[0]
min_num = nums[0]
total = 0
j = 0
while j < n:
    if nums[j] > max_num: max_num = nums[j]
    if nums[j] < min_num: min_num = nums[j]
    total += nums[j]
    j += 1
avg = total / n
count = 0
k = 0
while k < n:
    if nums[k] > avg: count += 1
    k += 1
print(f"Макс: {max_num}")
print(f"Мин: {min_num}")
print(f"Среднее: {avg:.2f}")
print(f"Больше среднего: {count}")