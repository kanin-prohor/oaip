def format_report(report_title: str, *data: str, **properties: str) -> None:
    
    print("=" * 50)
    print(f"ОТЧЕТ: {report_title}")
    print("=" * 50)
    
    if properties:
        print("\nМетаданные:")
        for key, value in properties.items():
            print(f"  {key}: {value}")
    
    if data:
        print("\nПункты отчета:")
        for i, item in enumerate(data, 1):
            print(f"  {i}. {item}")
    else:
        print("\nНет пунктов отчета")
    
    print("=" * 50)

format_report("Продажи за квартал", 
              "Рост на 15%", 
              "Новые клиенты: 25",
              author="Иванов",
              date="2024-01-15")

print("\n")

format_report("Ежедневный отчет",
              author="Сидорова",
              department="Бухгалтерия")