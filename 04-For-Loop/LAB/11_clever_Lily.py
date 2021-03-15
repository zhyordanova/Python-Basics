age = int(input())
laundry_price = float(input())
toy_price = int(input())

sum = 0
toy_count = 0
brother_money = 0

money = 0

for year in range(1, age + 1):
    if year % 2 == 0:
        money = money + 10
        sum += money
        brother_money += 1
    else:
        toy_count += 1

savings = sum + (toy_count * toy_price) - brother_money

if savings >= laundry_price:
    print(f"Yes! {savings - laundry_price:.2f}")
else:
    print(f"No! {laundry_price - savings:.2f}")
