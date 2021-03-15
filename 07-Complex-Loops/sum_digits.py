n = int(input())

sum_number = 0

while True:
    sum_number = sum_number + (n % 10)
    n = n // 10

    if not n > 0:
        break

print(f"Sum of digits: {sum_number}")
