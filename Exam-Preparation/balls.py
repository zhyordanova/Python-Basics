n = int(input())

total_points = 0
red_point = 0
orange_point = 0
yellow_point = 0
white_point = 0
black_point = 0
other_point = 0

for i in range(0, n):
    colors = input()

    if colors == 'red':
        red_point += 1
        total_points += 5
    elif colors == "orange":
        orange_point += 1
        total_points += 10
    elif colors == "yellow":
        yellow_point += 1
        total_points += 15
    elif colors == "white":
        white_point += 1
        total_points += 20
    elif colors == "black":
        black_point += 1
        total_points /= 2
    else:
        other_point += 1


print(f'Total points: {int(total_points)}')
print(f'Points from red balls: {red_point}')
print(f'Points from orange balls: {orange_point}')
print(f'Points from yellow balls: {yellow_point}')
print(f'Points from white balls: {white_point}')
print(f'Other colors picked: {other_point}')
print(f'Divides from black balls: {black_point}')
