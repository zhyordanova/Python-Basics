import math

guests = int(input())
budget = int(input())

count_easter_bread = math.ceil(guests / 3)
count_eggs = guests * 2

easter_bread_price = count_easter_bread * 4
egg_price = count_eggs * 0.45

needed_money = easter_bread_price + egg_price
diff = budget - needed_money

if needed_money <= budget:
    print(f'Lyubo bought {count_easter_bread} Easter bread and {count_eggs} eggs.\nHe has {diff:.2f} lv. left.')
else:
    print(f'Lyubo doesn\'t have enough money.\nHe needs {abs(diff):.2f} lv. more.')