#	"room for one person" – 18.00 лв за нощувка
#	"apartment" – 25.00 лв за нощувка
#	"president apartment" – 35.00 лв за нощувка

#(пример: 11 дни = 10 нощувки)

#позитивна, към цената с вече приспаднатото намаление добавя 25% от нея.
# Ако оценката му е негативна приспада от цената 10%.

day = int(input())
room = input()
feedback = input()

price = 0
nights = day - 1

if room == "room for one person":
    price = nights * 18
elif room == "apartment":
    if day <= 10:
        price = (nights * 25) * 0.7
    elif 10 < day <= 15:
        price = (nights * 25) * 0.65
    elif day > 15:
        price = (nights * 25) * 0.50
elif room == "president apartment":
    if day <= 10:
        price = (nights * 35) * 0.9
    elif 10 < day <= 15:
        price = (nights * 35) * 0.85
    elif day > 15:
        price = (nights * 35) * 0.80

if feedback == "positive":
    price = price * 1.25
else:
    price = price * 0.90

print(f"{price:.2f}")

