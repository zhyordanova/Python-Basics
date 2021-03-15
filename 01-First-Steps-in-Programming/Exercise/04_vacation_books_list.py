pages_number = int(input())
pages_per_hour = int(input())
days_count = int(input())

reading_time = pages_number / pages_per_hour
hours_per_day = reading_time / days_count

print(hours_per_day)