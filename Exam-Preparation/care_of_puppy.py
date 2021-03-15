food_kg = int(input())

puppy_food = food_kg * 1000

command = input()

while command != "Adopted":

    puppy_food -= int(command)

    if command == "Adopted":
        break

    command = input()

if puppy_food >= 0:
    print(f'Food is enough! Leftovers: {puppy_food} grams.')
else:
    print(f'Food is not enough. You need {abs(puppy_food)} grams more.')
