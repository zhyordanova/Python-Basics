customer = int(input())

total_price = 0
average_price = 0

for i in range(1, customer + 1):
    count_product = 0
    customer_spend = 0

    product = input()
    while product != "Finish":
        count_product += 1

        if product == "basket":
            price = 1.5
        elif product == "wreath":
            price = 3.8
        elif product == "chocolate bunny":
            price = 7

        customer_spend += price

        product = input()

    if count_product % 2 == 0:
        customer_spend *= 0.8

    print(f'You purchased {count_product} items for {customer_spend:.2f} leva.')

    total_price += customer_spend

average_price = total_price / customer

print(f'Average bill per client is: {average_price:.2f} leva.')

    
