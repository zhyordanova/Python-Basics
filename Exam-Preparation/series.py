budget = float(input())
n = int(input())

total_price = 0

for series in range (0, n):
    name = input()
    price = float(input())

    if name == "Thrones":
        price /= 2
    elif name == "Lucifer":
        price *= 0.6
    elif name == "Protector":
        price *= 0.7
    elif name == "TotalDrama":
        price *= 0.8
    elif name == "Area":
        price *= 0.9

    total_price += price

diff = budget - total_price

if budget >= total_price:
    print(f'You bought all the series and left with {diff:.2f} lv.')
else:
    print(f'You need {abs(diff):.2f} lv. more to buy the series!')
