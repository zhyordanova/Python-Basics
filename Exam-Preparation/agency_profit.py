name = input()
adult_ticket = int(input())
kid_ticket = int(input())
price_adult = float(input())
service_tax = float(input())

price_kid = price_adult * 0.3
price_tax_adult = price_adult + service_tax
price_tax_kid = price_kid + service_tax

total_price = (adult_ticket * price_tax_adult) + (kid_ticket * price_tax_kid)
profit = total_price * 0.2

print(f'The profit of your agency from {name} tickets is {profit:.2f} lv.')