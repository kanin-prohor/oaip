a, b, c = map(int, input("Введите три целых числа через пробел: ").split())
m1 = a * b
m2 = b * c
m3 = c * a
p4 = a ** 4
rem = b % c
div = c // a
print("Умножения:", f"{a}*{b}={m1}", f"{b}*{c}={m2}", f"{c}*{a}={m3}", sep=", ")
print("Доп. операции:", f"{a}^4={p4}", f"{b}%{c}={rem}", f"{c}//{a}={div}", sep=", ")
print("Сумма доп. операций:", f"{p4}+{rem}+{div}={p4 + rem + div}")