vacation_money = float(input())
owned_money = float(input())

days_counter = 0
spending_counter = 0

while owned_money <= vacation_money and spending_counter < 5:

    action = input()
    money = float(input())

    days_counter += 1

    if action == "save":
        owned_money += money
        spending_counter = 0
    elif action == "spend":
        owned_money -= money
        spending_counter += 1
        if owned_money < 0:
            owned_money = 0

    if owned_money >= vacation_money:
        break


if spending_counter == 5:
    print(f'You can\'t save the money.')
    print(days_counter)

if owned_money >= vacation_money:
    print(f'You saved the money for {days_counter} days.')