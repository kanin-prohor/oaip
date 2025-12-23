def calc_avg(numbers: list[float]) -> float:
    if not numbers:
        return 0.0
        
    return sum(numbers) / len(numbers)

def fmt_fio(parts: list[str], capitalize: bool = True) -> str:
    fio = " ".join(parts)
    
    if capitalize:
        return fio.title()
        
    return fio

def filter_scores(data_dict: dict[str, int], min_value: int) -> dict[str, int]:
    result = {}
    
    for key, value in data_dict.items():
        if value >= min_value:
            result[key] = value
            
    return result

if __name__ == "__main__":
    print("=== Функция calc_avg ===")
    print(f"calc_avg([10, 20, 30, 40]) = {calc_avg([10, 20, 30, 40])}")
    print(f"calc_avg([]) = {calc_avg([])}")
    print()
    
    print("=== Функция fmt_fio ===")
    print(f'fmt_fio(["петров", "иван", "сергеевич"]) = '
          f'{fmt_fio(["петров", "иван", "сергеевич"])}')
    print(f'fmt_fio(["сидорова", "анна", "валерьевна"], capitalize=False) = '
          f'{fmt_fio(["сидорова", "анна", "валерьевна"], capitalize=False)}')
    print()
    
    print("=== Функция filter_scores ===")
    scores = {"math": 95, "history": 78, "english": 88, "art": 92}
    print(f"scores = {scores}")
    print(f"filter_scores(scores, 90) = {filter_scores(scores, 90)}")
    print(f"filter_scores(scores, 80) = {filter_scores(scores, 80)}")