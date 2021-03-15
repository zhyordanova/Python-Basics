while True:
    destination = input()
    if destination == 'End':
        break
    budget = float(input())

    savings = 0
    while savings < budget:
        money = float(input())
        savings += money
    print(f'Going to {destination}!')