# цената на 1кв.м. = 7,61 лв. с ДДС
# 18% отстъпка от крайната цена

area = float(input())

price = area * 7.61
discount = price * 0.18
final_price = price - discount

print("The final price is: " + str(final_price) + " lv.")
print("The discount is: " + str(discount) + " lv.")