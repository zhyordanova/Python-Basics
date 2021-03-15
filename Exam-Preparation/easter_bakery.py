price_floor = float(input())
floor_kg = float(input())
sugar_kg = float(input())
cover_eggs = int(input())
yeast = int(input())

price_sugar = price_floor * 0.75
price_eggs = price_floor * 1.1
price_yeast = price_sugar * 0.2

sum_floor = floor_kg * price_floor
sum_sugar = sugar_kg* price_sugar
sum_eggs = cover_eggs * price_eggs
sum_yeast = yeast * price_yeast

total_sum = sum_floor + sum_sugar + sum_eggs + sum_yeast

print(f'{total_sum:.2f}')