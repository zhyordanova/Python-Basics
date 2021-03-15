sea = int(input())
mountain = int(input())

profit = 0

command = input()
while command != "Stop":

    if command == "sea":
        if sea > 0:
            profit += 680
            sea -= 1
    elif command == "mountain":
        if mountain > 0:
            profit += 499
            mountain -= 1

    if sea == 0 and mountain == 0:
        print('Good job! Everything is sold.')
        break

    command = input()

print(f'Profit: {profit} leva.')



