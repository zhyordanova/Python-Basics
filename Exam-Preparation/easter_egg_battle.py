first_player_eggs = int(input())
second_player_eggs = int(input())

while first_player_eggs > 0 and second_player_eggs > 0:

    line = input()

    if line == "one":
        second_player_eggs -= 1
    elif line == "two":
        first_player_eggs -= 1

    if line == "End of battle":
        break

if first_player_eggs <= 0:
    print(f'Player one is out of eggs. Player two has {second_player_eggs} eggs left.')
elif second_player_eggs <= 0:
    print(f'Player two is out of eggs. Player one has {first_player_eggs} eggs left.')
else:
  print(f'Player one has {first_player_eggs} eggs left.')
  print(f'Player two has {second_player_eggs} eggs left.')


