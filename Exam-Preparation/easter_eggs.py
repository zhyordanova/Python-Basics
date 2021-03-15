import sys
color_eggs = int(input())

red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_egg = 0
max_eggs = - sys.maxsize
wanted_color = ''

for i in range(0,  color_eggs):
    color = input()

    if color == "red":
        red_eggs += 1
    elif color == "orange":
        orange_eggs += 1
    elif color == "blue":
        blue_eggs += 1
    elif color == "green":
        green_egg += 1

    if red_eggs > max_eggs:
        max_eggs = red_eggs
        wanted_color = 'red'
    elif orange_eggs > max_eggs:
        max_eggs = orange_eggs
        wanted_color = 'orange'
    elif blue_eggs > max_eggs:
        max_eggs = blue_eggs
        wanted_color = 'blue'
    elif green_egg > max_eggs:
        max_eggs = green_egg
        wanted_color = 'green'

print(f'Red eggs: {red_eggs}')
print(f'Orange eggs: {orange_eggs}')
print(f'Blue eggs: {blue_eggs}')
print(f'Green eggs: {green_egg}')
print(f"Max eggs: {max_eggs} -> {wanted_color}")



