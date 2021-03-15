n = int(input())

percent_sales = 100 / n
Hearthstone_percent = 0
Fornite_percent = 0
Overwatch_percent = 0
Others_percent = 0


for i in range(0, n):
    name_game = input()

    if name_game == "Hearthstone":
        Hearthstone_percent += percent_sales
    elif name_game == "Fornite":
        Fornite_percent += percent_sales
    elif name_game == "Overwatch":
        Overwatch_percent += percent_sales
    else:
        Others_percent += percent_sales

print(f'Hearthstone - {Hearthstone_percent:.2f}%')
print(f'Fornite - {Fornite_percent:.2f}%')
print(f'Overwatch - {Overwatch_percent:.2f}%')
print(f'Others - {Others_percent:.2f}%')






