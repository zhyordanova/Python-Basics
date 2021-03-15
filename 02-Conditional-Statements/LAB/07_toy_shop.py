vacation_price = float(input())
count_puzzles = int(input())
count_dolls = int(input())
count_bears = int(input())
count_minions = int(input())
count_trucks = int(input())

price_puzzle = count_puzzles * 2.60
price_dolls = count_dolls * 3
price_bears = count_bears * 4.10
price_minions = count_minions * 8.20
price_trucks = count_trucks * 2

total_price = price_puzzle + price_dolls + price_bears + price_minions + price_trucks


total_count = count_puzzles + count_dolls + count_bears + count_minions + count_trucks

if total_count >= 50:
    total_price = total_price * 0.75

profit = total_price * 0.90

out_money = abs(profit - vacation_price)

if profit > vacation_price:
    print(f"Yes! {out_money:.2f} lv left.")
else:
    print(f"Not enough money! {out_money:.2f} lv needed.")