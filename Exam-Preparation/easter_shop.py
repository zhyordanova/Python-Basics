start_eggs = int(input())

buy_eggs = 0

line = input()

while line != "Close":

    if line == "Fill":
        additional_eggs = int(input())
        start_eggs += additional_eggs

    if line == "Buy":
        soled_eggs = int(input())

        if soled_eggs <= start_eggs:
            start_eggs -= soled_eggs
            buy_eggs += soled_eggs

        else:
            print(f'Not enough eggs in store!\nYou can buy only {start_eggs}.')
            break

    line = input()

    if line == "Close":
        print(f'Store is closed!\n{buy_eggs} eggs sold.')

