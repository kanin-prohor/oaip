n = int(input("Введите высоту пирамиды: "))
i = 1
while i <= n:
    spaces = n - i
    j = 0
    while j < spaces:
        print(" ", end=" ")
        j += 1
    k = 1
    while k <= i:
        print(k, end=" ")
        k += 1
    m = i - 1
    while m >= 1:
        print(m, end=" ")
        m -= 1
    print()
    i += 1