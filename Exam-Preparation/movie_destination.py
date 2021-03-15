budget = float(input())
destination = input()
season = input()
days = int(input())

price = 0

if season == "Winter":
    if destination == "Dubai":
        price = 45000
    elif destination == "Sofia":
        price = 17000
    elif destination == "London":
        price = 24000
elif season == "Summer":
    if destination == "Dubai":
        price = 40000
    elif destination == "Sofia":
        price = 12500
    elif destination == "London":
        price = 20250

total_price = days * price

if destination == "Dubai":
    total_price *= 0.7
elif destination == "Sofia":
    total_price *= 1.25

diff = total_price - budget

if total_price <= budget:
    print(f'The budget for the movie is enough! We have {abs(diff):.2f} leva left!')
else:
    print(f'The director needs {abs(diff):.2f} leva more!')