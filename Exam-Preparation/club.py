wanted_profit = float(input())

order_price = 0
income = 0

name_cocktail = input()
while name_cocktail != "Party!":
    count_cocktails = int(input())

    cocktail_price = 0
    for letter in name_cocktail:
        cocktail_price += 1

    order_price = count_cocktails * cocktail_price

    if order_price % 2 == 1:
        order_price *= 0.75

    income += order_price

    if wanted_profit <= income:
        break

    name_cocktail = input()

if wanted_profit <= income:
    print('Target acquired.')
else:
    print(f'We need {wanted_profit - income:.2f} leva more.')

print(f'Club income - {income:.2f} leva.')




