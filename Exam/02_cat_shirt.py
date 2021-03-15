sleeve = float(input())
front = float(input())
type_fabric = input()
tie = input()
price_shirt = 0

size_shirt = (sleeve * 2 + front * 2) * 1.1
size_m = size_shirt / 100

if type_fabric == "Linen":
    price_shirt = size_m * 15 + 10
elif type_fabric == "Cotton":
    price_shirt = size_m * 12 + 10
elif type_fabric == "Denim":
    price_shirt = size_m * 20 + 10
elif type_fabric == "Twill":
    price_shirt = size_m * 16 + 10
elif type_fabric == "Flannel":
    price_shirt = size_m * 11 + 10

if tie == "Yes":
    price_shirt *= 1.2

print(f'The price of the shirt is: {price_shirt:.2f}lv.')
