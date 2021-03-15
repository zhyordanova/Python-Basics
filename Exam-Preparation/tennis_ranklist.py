import math

count_tournament = int(input())
beginning_point = int(input())

final_score = 0
won_tournament = 0
total_points = 0
average_point = 0
percent_won_tournament = 0

for tournament in range(0, count_tournament):
    stage = input()

    if stage == "W":
        final_score += 2000
        won_tournament += 1
    elif stage == "F":
        final_score += 1200
    else:
        final_score += 720

    total_points = beginning_point + final_score
    average_point = final_score / count_tournament

    percent_won_tournament = (won_tournament / count_tournament) * 100

print(f'Final points: {total_points}')
print(f'Average points: {math.floor(average_point)}')
print(f'{percent_won_tournament:.2f}%')
