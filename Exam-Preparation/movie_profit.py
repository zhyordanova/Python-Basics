name = input()
days = int(input())
tickets = int(input())
ticket_price = float(input())
percent_cinema = float(input())

price_day = tickets * ticket_price
total_price = days * price_day
percent_profit = total_price * percent_cinema / 100
profit = total_price - percent_profit

print(f'The profit from the movie {name} is {profit:.2f} lv.')