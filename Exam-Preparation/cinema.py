capacity = int(input())

total_sum = 0

line = input()
while line != "Movie time!":
    count_people = int(line)
    capacity -= count_people

    if capacity < 0:
        break

    if count_people % 3 == 0:
        total_sum += (count_people * 5) - 5
    else:
        total_sum += count_people * 5

    line = input()

if capacity >= 0:
    print(f'There are {capacity} seats left in the cinema.')
else:
    print('The cinema is full.')

print(f'Cinema income - {total_sum} lv.')