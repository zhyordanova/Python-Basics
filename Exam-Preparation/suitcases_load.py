truck_capacity = float(input())

counter = 0

line = input()
while line != "End":
    suitcases = float(line)

    if (counter + 1) % 3 == 0:
        suitcases += suitcases * 0.1

    if truck_capacity < suitcases:
        print(f'No more space!')
        break

    counter += 1
    truck_capacity -= suitcases

    line = input()

if line == "End":
    print(f'Congratulations! All suitcases are loaded!')

print(f'Statistic: {counter} suitcases loaded.')










