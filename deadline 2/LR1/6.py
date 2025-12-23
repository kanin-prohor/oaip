symbol = input("Введите символ для рисования: ")
height = int(input("Введите высоту прямоугольника: "))
width = int(input("Введите ширину прямоугольника: "))
i = 0
while i < height:
    j = 0
    row = ""
    while j < width:
        row += symbol
        j += 1
    print(row)
    i += 1