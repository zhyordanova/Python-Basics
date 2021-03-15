budget = float(input())
fuel = float(input())
day = input()

fuel_price = fuel * 2.1
excursion = fuel_price + 100

if day == "Saturday":
    excursion *= 0.9
else:
    excursion *= 0.8

diff = budget - excursion

if excursion <= budget:
    print(f'Safari time! Money left: {diff:.2f} lv.')
else:
    print(f'Not enough money! Money needed: {abs(diff):.2f} lv.')


