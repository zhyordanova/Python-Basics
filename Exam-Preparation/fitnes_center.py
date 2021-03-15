people = int(input())

back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0
work_out = 0
buy_products = 0
average_work_out = 0
average_buy = 0

for person in range(0, people):
    activity = input()

    if activity == "Back":
        back += 1
        work_out += 1
    elif activity == "Chest":
        chest += 1
        work_out += 1
    elif activity == "Legs":
        legs += 1
        work_out += 1
    elif activity == "Abs":
        abs += 1
        work_out += 1
    elif activity == "Protein shake":
        protein_shake += 1
        buy_products += 1
    elif activity == "Protein bar":
        protein_bar += 1
        buy_products += 1

average_work_out = work_out / people * 100
average_buy = buy_products / people * 100

print(f'{back} - back')
print(f'{chest} - chest')
print(f'{legs} - legs')
print(f'{abs} - abs')
print(f'{protein_shake} - protein shake')
print(f'{protein_bar} - protein bar')
print(f'{average_work_out:.2f}% - work out')
print(f'{average_buy:.2f}% - protein')