import math
import sys
easter_bread = int(input())

total_sugar = 0
total_flour = 0

packs_sugar = 0
packs_flour = 0

max_sugar = -sys.maxsize
max_flour = -sys.maxsize

for i in range(0, easter_bread):
    sugar = int(input())
    flour = int(input())

    total_sugar += sugar
    total_flour += flour

    packs_sugar = math.ceil(total_sugar / 950)
    packs_flour = math.ceil(total_flour / 750)

    if sugar > max_sugar:
        max_sugar = sugar
    if flour > max_flour:
        max_flour = flour

print(f'Sugar: {packs_sugar}')
print(f'Flour: {packs_flour}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')


