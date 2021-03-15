destination = input()
date = input()
nights = int(input())

price_night = 0

if destination == "France":
    if date == "21-23":
        price_night = 30
    elif date == "24-27":
        price_night = 35
    elif date == "28-31":
        price_night = 40
elif destination == "Italy":
    if date == "21-23":
        price_night = 28
    elif date == "24-27":
        price_night = 32
    elif date == "28-31":
        price_night = 39
elif destination == "Germany":
    if date == "21-23":
        price_night = 32
    elif date == "24-27":
        price_night = 37
    elif date == "28-31":
        price_night = 43

cost_excursion = nights * price_night

print(f'Easter trip to {destination} : {cost_excursion:.2f} leva.')


