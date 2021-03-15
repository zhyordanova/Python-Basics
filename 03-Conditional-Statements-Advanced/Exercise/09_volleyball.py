import math
year = input()
holidays = int(input())
weekend_home = int(input())

weekend__sofia = 48 - weekend_home
play_sofia = weekend__sofia * 3/4
holiday_play = holidays * 2/3

total_play = play_sofia + weekend_home + holiday_play

if year == "leap":
    total_play = total_play + (total_play * 0.15)
else:
    total_play

print(math.floor(total_play))