n = int(input())

p_1 = 0
p_2 = 0
p_3 = 0

for i in range(0, n):
    number = int(input())

    if number % 2 == 0:
        p_1 += 1

    if number % 3 == 0:
        p_2 += 1

    if number % 4 == 0:
        p_3 += 1

percent_p1 = p_1 / n * 100
percent_p2 = p_2 / n * 100
percent_p3 = p_3 / n * 100

print(f'{percent_p1:.2f}%')
print(f'{percent_p2:.2f}%')
print(f'{percent_p3:.2f}%')
