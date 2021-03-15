import math
name = input()
seasons = int(input())
series = int(input())
real_time = float(input())

promotions = real_time * 0.2
duration_series = real_time + promotions
special_series = seasons * 10
total_time = duration_series * series * seasons + special_series

print(f'Total time needed to watch the {name} series is {math.ceil(total_time)} minutes.')