result = 0
list_of_squares = []

for x in range(548001):
    list_of_squares.append(x**2)

for i, x in enumerate(list_of_squares):
    if i % 2 != 0:
        result += x

print(result)

# Registration: Find the odd-numbered squares of the first 548 thousand numbers