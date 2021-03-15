fruit = input()
size = input()
set_count = int(input())

pack = 0
price_pack=0

if size == "small":
    pack = 2
    if fruit == "Watermelon":
        price_pack = pack * 56
    elif fruit == "Mango":
        price_pack = pack * 36.66
    elif fruit == "Pineapple":
        price_pack = pack * 42.10
    elif fruit == "Raspberry":
        price_pack = pack * 20
else:
    pack = 5
    if fruit == "Watermelon":
        price_pack = pack * 28.70
    elif fruit == "Mango":
        price_pack = pack * 19.60
    elif fruit == "Pineapple":
        price_pack = pack * 24.80
    elif fruit == "Raspberry":
        price_pack = pack * 15.20

total_price = price_pack * set_count

if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price >1000:
    total_price *= 0.50

print(f'{total_price:.2f} lv.')


