tournament_days = int(input())

total_money = 0
total_wins = 0
total_lost = 0

for day in range(0, tournament_days):

    sport = input()
    win_money_day = 0
    win_counter = 0
    lose_counter = 0

    while sport != "Finish":
        result = input()

        if result == "win":
            win_counter += 1
            win_money_day += 20
            total_wins += 1
        else:
            lose_counter += 1
            total_lost += 1

        sport = input()

    if win_counter > lose_counter:
        win_money_day *= 1.1

    total_money += win_money_day

if total_wins > total_lost:
    total_money *= 1.2
    print(f'You won the tournament! Total raised money: {total_money:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_money:.2f}')

