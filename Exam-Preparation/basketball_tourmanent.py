total_count_game = 0
win_count = 0
lost_count = 0
percent_win = 0
percent_lost = 0

name_tournament = input()
while name_tournament != "End of tournaments":
    count_game = int(input())

    current_name = name_tournament

    for game in range(1, count_game + 1):
        points_Desi = int(input())
        points_opponents = int(input())

        win_diff = 0
        lost_diff= 0

        if points_Desi > points_opponents:
            total_count_game += 1
            win_count += 1
            win_diff = points_Desi - points_opponents
            print(f'Game {game} of tournament {current_name}: win with {win_diff} points.')
        else:
            total_count_game += 1
            lost_count += 1
            lost_diff = points_opponents - points_Desi
            print(f'Game {game} of tournament {current_name}: lost with {lost_diff} points.')

    percent_win = win_count / total_count_game * 100
    percent_lost = lost_count / total_count_game * 100

    name_tournament = input()

print(f'{percent_win:.2f}% matches win')
print(f'{percent_lost:.2f}% matches lost')

