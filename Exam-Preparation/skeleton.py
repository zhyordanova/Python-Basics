mins_control = int(input())
sec_control = int(input())
length = float(input())
meters_sec = int(input())

control_seconds = mins_control * 60 + sec_control
slope = length / 120
reduced_time = slope * 2.5

Martin_time = (length / 100) * meters_sec - reduced_time

if Martin_time <= control_seconds:
    print(f'Marin Bangiev won an Olympic quota!\nHis time is {Martin_time:.3f}.')
else:
    print(f'No, Marin failed! He was {Martin_time - control_seconds:.3f} second slower.')