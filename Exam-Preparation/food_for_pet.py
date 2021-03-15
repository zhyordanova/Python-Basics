count_days = int(input())
total_food = float(input())

day_food = 0
total_dog = 0
total_cat = 0
eaten_together = 0
biscuits = 0

for day in range(1, count_days + 1):
    dog_food = int(input())
    total_dog += dog_food
    cat_food = int(input())
    total_cat += cat_food

    if day %3 == 0:
        current_biscuits = (dog_food + cat_food) * 0.1
        biscuits += current_biscuits

eaten_together = total_dog + total_cat
percent_food = eaten_together / total_food * 100
percent_dog = total_dog / eaten_together * 100
percent_cat = total_cat / eaten_together * 100

print(f'Total eaten biscuits: {round(biscuits)}gr.')
print(f'{percent_food:.2f}% of the food has been eaten.')
print(f'{percent_dog:.2f}% eaten from the dog.')
print(f'{percent_cat:.2f}% eaten from the cat.')
