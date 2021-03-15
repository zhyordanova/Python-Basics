count = int(input())
type_joinery = input()
delivery = input()

price = 0

if type_joinery == "90X130":
    price = 110
    if 30 < count < 60:
        price *= 0.95
    elif count > 60:
        price *= 0.92
elif type_joinery == "100X150":
    price = 140
    if 40 < count < 80:
        price *= 0.94
    elif count > 80:
        price *= 0.90
elif type_joinery == "130X180":
    price = 190
    if 20 < count < 50:
        price *= 0.93
    elif count > 50:
        price *= 0.88
else:
    price = 250
    if 25 < count < 50:
        price *= 0.91
    elif count > 50:
        price *= 0.86

total_price = count * price

if delivery == 'With delivery':
    total_price += 60

if count > 99:
    total_price *= 0.96

if count <= 10:
    print('Invalid order')
else:
    print(f'{total_price:.2f} BGN')

