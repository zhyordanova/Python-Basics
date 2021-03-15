import sys

n = int(input())

sum_nums = 0
max_num = -sys.maxsize

for i in range(0,n):
    number = int(input())
    sum_nums += number
    if number > max_num:
        max_num = number

new_sum = sum_nums - max_num

if new_sum == max_num:
    print(f"Yes \nSum = {new_sum}")
else:
    print(f"No \nDiff = {abs(max_num - new_sum)}")
