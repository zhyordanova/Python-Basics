n = int(input())

number = 1

for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(number, end=' ')
        number += 1

        if col >= row:
            print()
        if number > n:
            break

    if number > n:
        break
