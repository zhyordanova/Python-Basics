import math
price_one_racket = float(input())
tennis_racket = int(input())
sneakers = int(input())

price_rackets = tennis_racket * price_one_racket
price_pair_sneakers = price_one_racket / 6
price_sneakers = sneakers * price_pair_sneakers

other_equipment = (price_rackets + price_sneakers) * 0.2

total_price = price_rackets + price_sneakers + other_equipment

Djokovic = total_price / 8
sponsors = total_price * 7 / 8

print(f'Price to be paid by Djokovic {math.floor(Djokovic)}')
print(f'Price to be paid by sponsors {math.ceil(sponsors)}')
