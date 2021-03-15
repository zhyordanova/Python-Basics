pens_pack = int(input())
markers_pack = int(input())
cleaner = float(input())
discount = int(input())

pens_price = pens_pack * 5.8
markers_price = markers_pack * 7.20
cleaner_price = cleaner * 1.20

total_sum = pens_price + markers_price + cleaner_price
sum_after_discount = total_sum - ((total_sum * discount) / 100)

print(f'{sum_after_discount:.3f}')