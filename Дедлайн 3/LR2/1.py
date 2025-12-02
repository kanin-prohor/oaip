def squares_gen(n):
    for i in range(1, n + 1):
        yield i ** 2

for square in squares_gen(5):
    print(square)

squares = list(squares_gen(5))
print(squares)