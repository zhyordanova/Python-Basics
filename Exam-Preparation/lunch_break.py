import math
name = input()
duration_series = int(input())
break_duration = int(input())

lunch_time = break_duration * 1/8
break_time = break_duration * 1/4
left_time = break_duration - lunch_time - break_time

if left_time >= duration_series:
    print(f'You have enough time to watch {name} and left with {math.ceil(left_time - duration_series)} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {name}, you need {math.ceil(duration_series - left_time)} more minutes.')
