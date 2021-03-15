number = int(input())

fact = 1

while True:
    fact *= number

    number -= 1

    if not number > 1:
        break

print(fact)