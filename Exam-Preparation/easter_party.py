guests = int(input())
price_per_person = float(input())
budget = float(input())

if 10 <= guests <= 15:
    price_per_person *= 0.85
elif 15 < guests <= 20:
    price_per_person *= 0.8
elif guests > 20:
    price_per_person *= 0.75

money_for_guest = guests * price_per_person
cake = budget * 0.1

total_sum = money_for_guest + cake

diff = budget - total_sum

if total_sum <= budget:
    print(f'It is party time! {diff:.2f} leva left.')
else:
    print(f'No party! {abs(diff):.2f} leva needed.')
