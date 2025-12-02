import random
temps = [round(random.uniform(-10, 15), 1) for _ in range(14)]
print(f"Температуры: {temps}")
print(f"Макс: {max(temps)}°C, Мин: {min(temps)}°C")
avg = sum(temps)/len(temps)
print(f"Средняя: {avg:.1f}°C")
above_avg = sum(1 for t in temps if t > avg)
print(f"Дней выше средней: {above_avg}")
print(f"Сортировка: {sorted(temps)}")
f_temps = [round(t * 9/5 + 32, 1) for t in temps]
print(f"Фаренгейты: {f_temps}")