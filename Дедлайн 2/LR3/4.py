products = {
    "Ноутбук": {"price": 50000, "sold": 15},
    "Мышь": {"price": 1000, "sold": 45},
    "Клавиатура": {"price": 2500, "sold": 30},
    "Монитор": {"price": 30000, "sold": 8}
}
most_sold_product = None
max_sold = 0
for product, details in products.items():
    if details["sold"] > max_sold:
        max_sold = details["sold"]
        most_sold_product = product
print(f"1. Самый продаваемый товар: {most_sold_product} (продано {max_sold} шт.)")
total_revenue = 0
for product, details in products.items():
    revenue = details["price"] * details["sold"]
    total_revenue += revenue
print(f"2. Общая выручка магазина: {total_revenue:,} руб.")
most_revenue_product = None
max_revenue = 0
for product, details in products.items():
    revenue = details["price"] * details["sold"]
    if revenue > max_revenue:
        max_revenue = revenue
        most_revenue_product = product
print(f"3. Товар с наибольшей выручкой: {most_revenue_product} ({max_revenue:,} руб.)")
print("\n" + "="*50)
print("ДЕТАЛЬНАЯ СТАТИСТИКА ПО ТОВАРАМ:")
print("="*50)
product_stats = []
for product, details in products.items():
    revenue = details["price"] * details["sold"]
    product_stats.append((product, details["sold"], revenue))
product_stats.sort(key=lambda x: x[2], reverse=True)
print(f"{'Товар':<15} {'Продано, шт.':<15} {'Выручка, руб.':<20}")
print("-"*50)
for product, sold, revenue in product_stats:
    print(f"{product:<15} {sold:<15} {revenue:<20,}")