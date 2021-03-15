shooting_time = int(input())
scene = int(input())
time_scene = int(input())

preparation = shooting_time * 0.15
time = scene * time_scene
needed_time = preparation + time

diff = shooting_time - needed_time

if needed_time <= shooting_time:
    print(f'You managed to finish the movie on time! You have {round(diff)} minutes left!')
else:
    print(f'Time is up! To complete the movie you need {round(abs(diff))} minutes.')