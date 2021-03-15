name = input()
game_season = int(input())

counter_score = 0
won = 0
equal = 0
lost = 0
percent_games = 0

for game in range(0, game_season):
    score = input()

    if score == "W":
        won += 1
        counter_score += 3
    elif score == "D":
        equal += 1
        counter_score += 1
    else:
        lost += 1

    percent_games = won / game_season * 100

if game_season == 0:
    print(f'{name} hasn\'t played any games during this season.')
else:
    print(f'{name} has won {counter_score} points during this season.')
    print(f'Total stats:')
    print(f'## W: {won}')
    print(f'## D: {equal}')
    print(f'## L: {lost}')
    print(f'Win rate: {percent_games:.2f}%')


