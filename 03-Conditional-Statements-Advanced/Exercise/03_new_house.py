flowers = input()
count_flowers = int(input())
budget = int(input())

if flowers == "Roses":
    price_flowers = count_flowers * 5
    if count_flowers > 80:
        price_flowers *= 0.9
elif flowers == "Dahlias":
    price_flowers = count_flowers * 3.8
    if count_flowers > 90:
        price_flowers *= 0.85
elif flowers == "Tulips":
    price_flowers = count_flowers * 2.8
    if count_flowers > 80:
        price_flowers *= 0.85
elif flowers == "Narcissus":
    price_flowers = count_flowers * 3
    if count_flowers < 120:
        price_flowers *= 1.15
else:
    price_flowers = count_flowers * 2.50
    if count_flowers < 80:
        price_flowers *= 1.2

if budget >= price_flowers:
    print(f"Hey, you have a great garden with {count_flowers} {flowers} and {budget - price_flowers:.2f} leva left.")
else:
    print(f"Not enough money, you need {price_flowers - budget:.2f} leva more.")
