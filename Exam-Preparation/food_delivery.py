chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

chicken_price = chicken_menu * 10.35
fish_price = fish_menu * 12.4
vegetarian_price = vegetarian_menu * 8.15

total_price = chicken_price + fish_price + vegetarian_price
dessert = total_price * 0.2
check = total_price + dessert + 2.5

print(f'Total: {check:.2f}')

