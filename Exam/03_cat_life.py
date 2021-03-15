import math
species = input()
gender = input()

human_years = 0
cat_months = 0

if species == "British Shorthair":
    if gender == "m":
        human_years = 13 * 12
        cat_months = human_years / 6
    else:
        human_years = 14 * 12
        cat_months = human_years / 6
    print(f'{math.floor(cat_months)} cat months')
elif species == "Siamese":
    if gender == "m":
        human_years = 15 * 12
        cat_months = human_years / 6
    else:
        human_years = 16 * 12
        cat_months = human_years / 6
    print(f'{math.floor(cat_months)} cat months')
elif species == "Persian":
    if gender == "m":
        human_years = 14 * 12
        cat_months = human_years / 6
    else:
        human_years = 15 * 12
        cat_months = human_years / 6
    print(f'{math.floor(cat_months)} cat months')
elif species == "Ragdoll":
    if gender == "m":
        human_years = 16 * 12
        cat_months = human_years / 6
    else:
        human_years = 17 * 12
        cat_months = human_years / 6
    print(f'{math.floor(cat_months)} cat months')
elif species == "American Shorthair":
    if gender == "m":
        human_years = 12 * 12
        cat_months = human_years / 6
    else:
        human_years = 13 * 12
        cat_months = human_years / 6
    print(f'{math.floor(cat_months)} cat months')
elif species == "Siberian":
    if gender == "m":
        human_years = 11 * 12
        cat_months = human_years / 6
    else:
        human_years = 12 * 12
        cat_months = human_years / 6
    print(f'{math.floor(cat_months)} cat months')
else:
    print(f'{species} is invalid cat!')





