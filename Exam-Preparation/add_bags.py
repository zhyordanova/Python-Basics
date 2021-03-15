baggage_over_20 = float(input())
kg_baggage = float(input())
day_till = int(input())
count_baggage = int(input())

price = 0

if kg_baggage < 10:
    price = baggage_over_20 * 0.2
elif 10 <= kg_baggage <= 20:
    price = baggage_over_20 / 2
elif kg_baggage > 20:
    price = baggage_over_20

if day_till > 30:
    price *= 1.1
elif 7 <= day_till <= 30:
    price *= 1.15
else:
    price *= 1.4

print(f'The total price of bags is: {(count_baggage * price):.2f} lv.')
