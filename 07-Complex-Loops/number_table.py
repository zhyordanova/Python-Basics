n = int(input())

for row in range(0, n, 1):
    for col in range(0, n, 1):
        number = row + col + 1

        if number > n:
            number = 2 * n - number
        print(number, end='')
    print()
