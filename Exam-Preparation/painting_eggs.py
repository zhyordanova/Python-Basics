size = input()
color = input()
batch = int(input())

price_egg = 0

if size == "Large":
    if color == "Red":
        price_egg = 16
    elif color == "Green":
        price_egg = 12
    elif color == "Yellow":
        price_egg = 9
elif size == "Medium":
    if color == "Red":
        price_egg = 13
    elif color == "Green":
        price_egg = 9
    elif color == "Yellow":
        price_egg = 7
if size == "Small":
    if color == "Red":
        price_egg = 9
    elif color == "Green":
        price_egg = 8
    elif color == "Yellow":
        price_egg = 5

batch_price = batch * price_egg
final_price = batch_price * 0.65

print(f'{final_price:.2f} leva.')
