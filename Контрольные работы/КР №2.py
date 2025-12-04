def print_receipt(date, *items, discount=0):
    print(f"Дата: {date}")
    print("Товары:")
    
    total = 0
    for name, price, qty in items:
        cost = price * qty
        total += cost
        print(f"  {name} ...... {qty} x {price} = {cost}")
    
    print(f"Промежуточный итог: {total}")
    
    discount_amount = total * discount / 100
    final_total = total - discount_amount
    
    if discount > 0:
        print(f"Скидка ({discount}%): {discount_amount:.2f}")
    
    print(f"Итого к оплате: {final_total:.2f}")

# Пример вызова
print_receipt(
    "2024-12-20",
    ("Хлеб", 50, 2),
    ("Молоко", 80, 1),
    ("Яблоки", 120, 3),
    discount=10
)