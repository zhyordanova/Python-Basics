bitcoins = int(input())
uan = float(input())
commission = float(input())

bitcoins_to_BGN = bitcoins * 1168
uan_to_BGN = uan * 0.15 * 1.76

total_euro = (bitcoins_to_BGN + uan_to_BGN) / 1.95

sum_commission = total_euro * commission / 100

result = total_euro - sum_commission

print(f'{result:.2f}')