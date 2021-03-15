name = input()
package = input()
tickets = int(input())

price = 0

if name == "John Wick":
    if package == "Drink":
        price = 12
    elif package == "Popcorn":
        price = 15
    else:
        price = 19
elif name == "Star Wars":
    if package == "Drink":
        price = 18
    elif package == "Popcorn":
        price = 25
    else:
        price = 30
elif name == "Jumanji":
    if package == "Drink":
        price = 9
    elif package == "Popcorn":
        price = 11
    else:
        price = 14

ticket_price = tickets * price

if name == "Star Wars" and tickets >= 4:
    ticket_price *= 0.7
elif name == "Jumanji" and tickets == 2:
    ticket_price *= 0.85

print(f'Your bill is {ticket_price:.2f} leva.')
