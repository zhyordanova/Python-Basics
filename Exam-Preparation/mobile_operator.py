tern = input()
contract = input()
internet = input()
months = int(input())

if tern == "one":
    if contract == "Small":
        price = 9.98
    elif contract == "Middle":
        price = 18.99
    elif contract == "Large":
        price = 25.98
    else:
        price = 35.99
elif tern == "two":
    if contract == "Small":
        price = 8.58
    elif contract == "Middle":
        price = 17.09
    elif contract == "Large":
        price = 23.59
    else:
        price = 31.79

if internet == "yes":
    if price <= 10:
        price += 5.5
    elif price <= 30:
        price += 4.35
    else:
        price += 3.85

if tern == "two":
    price *= 0.9625


print(f'{(price * months):.2f} lv.')

