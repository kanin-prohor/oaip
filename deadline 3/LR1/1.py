def create_counter():
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

counter1 = create_counter()
print(counter1())
print(counter1())
print(counter1())

counter2 = create_counter()
print(counter2())
print(counter1())