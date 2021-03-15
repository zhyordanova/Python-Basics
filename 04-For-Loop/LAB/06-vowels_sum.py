text = input()

sum_letter = 0

for letter in text:
    if letter == "a":
        sum_letter += 1
    elif letter =="e":
        sum_letter += 2
    elif letter == "i":
        sum_letter += 3
    elif letter == "o":
        sum_letter += 4
    elif letter == "u":
        sum_letter += 5

print(sum_letter)


