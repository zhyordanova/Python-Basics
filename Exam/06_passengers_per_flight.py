import sys
import math

airline = int(input())

max_passengers = -sys.maxsize
max_name = ''

for name in range(1, airline + 1):
    name_airline = input()
    current_name = ''

    passengers = input()

    average = 0
    counter = 0
    total_passengers = 0

    while passengers != "Finish":
        total_passengers += int(passengers)
        counter += 1

        passengers = input()

    current_name = name_airline

    average += total_passengers / counter

    if average > max_passengers:
        max_passengers = average
        max_name = current_name

    print(f'{current_name}: {math.floor(average)} passengers.')

print(f'{max_name} has most passengers per flight: {math.floor(max_passengers)}')















