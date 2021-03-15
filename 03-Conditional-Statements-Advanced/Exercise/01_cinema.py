type = input()
rows = int(input())
columns = int(input())

incomes = 0
full = rows * columns

if type == "Premiere":
    incomes = full * 12
elif type == "Normal":
    incomes = full * 7.5
else:
    incomes = full * 5

print(f"{incomes:.2f}")