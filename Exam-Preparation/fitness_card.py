our_sum = float(input())
gender = input()
age = int(input())
sport = input()

cart_price = 0

if gender == "m":
    if sport == "Gym":
        cart_price = 42
    elif sport == "Boxing":
        cart_price = 41
    elif sport == "Yoga":
        cart_price = 45
    elif sport == "Zumba":
        cart_price = 34
    elif sport == "Dances":
        cart_price = 51
    elif sport == "Pilates":
        cart_price = 39
elif gender == "f":
    if sport == "Gym":
        cart_price = 35
    elif sport == "Boxing":
        cart_price = 37
    elif sport == "Yoga":
        cart_price = 42
    elif sport == "Zumba":
        cart_price = 31
    elif sport == "Dances":
        cart_price = 53
    elif sport == "Pilates":
        cart_price = 37

if age <= 19:
    cart_price *= 0.8

if our_sum >= cart_price:
    print(f'You purchased a 1 month pass for {sport}.')
else:
    print(f'You don\'t have enough money! You need ${cart_price - our_sum:.2f} more.')
