budget = float(input())

count_product = 0
total_price = 0

product = input()

while product != "Stop":
    count_product += 1
    price = float(input())

    if count_product % 3 == 0:
        price /= 2

    total_price += price

    if total_price > budget:
        break

    product = input()

if total_price <= budget:
    print(f'You bought {count_product} products for {total_price:.2f} leva.')
else:
    print(f'You don\'t have enough money!\nYou need {abs(budget - total_price):.2f} leva!')




