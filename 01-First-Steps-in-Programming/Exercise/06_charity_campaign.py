# 1/8 от крайната сума ще бъде използвана за покриване на разходите за продуктите по време на кампанията.

days = int(input())
backers = int(input())
count_cakes = int(input())
count_waffles = int(input())
count_pancakes = int(input())

price_cake = 45
price_waffle = 5.80
price_pancake = 3.20

cakes = count_cakes * price_cake
waffles = count_waffles * price_waffle
pancakes = count_pancakes * price_pancake

total_sum_per_day = backers * (cakes + waffles + pancakes)
sum_campaign = total_sum_per_day * days
cost = 1/8 * sum_campaign

final_sum = sum_campaign - cost
print(final_sum)
