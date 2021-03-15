minutes_walk_per_day = int(input())
count_walk = int(input())
calories = int(input())

total_min_walk = minutes_walk_per_day * count_walk
burn_calories = total_min_walk * 5
percent_calories = calories * 0.5

if burn_calories >= percent_calories:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {burn_calories}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {burn_calories}.')

