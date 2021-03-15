# •	цената на  малините е на половина по-ниска от тази на ягодите;
# •	цената на портокалите е с 40% по-ниска от цената на малините;
# •	цената на бананите е с 80% по-ниска от цената на малините.

price_strawberries = float(input())
quantity_bananas = float(input())
quantity_oranges = float(input())
quantity_raspberries = float(input())
quantity_strawberries = float(input())

price_raspberries = price_strawberries / 2
price_oranges = (price_raspberries - (0.40 * price_raspberries))
price_bananas = (price_raspberries - (0.80 * price_raspberries))

strawberries = quantity_strawberries * price_strawberries
bananas = quantity_bananas * price_bananas
oranges = quantity_oranges * price_oranges
raspberries = quantity_raspberries * price_raspberries

total = strawberries + bananas + oranges + raspberries
print(total)