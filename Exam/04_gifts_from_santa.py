N = int(input())
M = int(input())
stop_adress = int(input())

for i in range(M, N - 1, -1):
    if i % 2 == 0 and i % 3 == 0 and i != stop_adress:
        print(i, end=' ')
    elif i % 2 == 0 and i % 3 == 0 and i == stop_adress:
        break
