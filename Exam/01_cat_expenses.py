bed_price = float(input())
toilet_price = float(input())

food_price = toilet_price * 1.25
toys_price = food_price / 2
vet = toys_price * 1.1
total_cost = toilet_price + food_price + toys_price + vet
other_cost = total_cost * 0.05

cost_year = bed_price + 12 * total_cost +12 * other_cost

print(f'{cost_year:.2f} lv.')