import math
record_sec = float(input())
distance_meters = float(input())
time_per_meter = float(input())

time_hike = distance_meters * time_per_meter
incline = math.floor(distance_meters / 50) * 30
total_time_hike = time_hike + incline

if record_sec <= total_time_hike:
    print(f'No! He was {total_time_hike - record_sec:.2f} seconds slower.')
else:
    print(f'Yes! The new record is {total_time_hike:.2f} seconds.')