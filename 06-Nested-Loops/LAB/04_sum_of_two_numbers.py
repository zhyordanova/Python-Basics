start_num = int(input())
end_num = int(input())
magic_number = int(input())

combination = 0
is_found = False

for num_1 in range(start_num, end_num + 1):
    if is_found:
        break
    for num_2 in range(start_num, end_num + 1):
        combination += 1

        if num_1 + num_2 == magic_number:
            is_found = True
            print(f'Combination N:{combination} ({num_1} + {num_2} = {magic_number})')
            break


if not is_found:
    print(f'{combination} combinations - neither equals {magic_number}')