month = input()
nights = int(input())

apartment = 0
studio = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
elif month == "June" or month == "September":
    studio = 75.2
    apartment = 68.7
elif month == "July" or month == "August":
    studio = 76
    apartment = 77

discount_apartment = 0
discount_studio = 0

if nights > 14:
    discount_apartment = 0.1
    if month == "May" or month == "October":
        discount_studio = 0.3
    elif month == "June" or month == "September":
        discount_studio = 0.2
elif nights > 7:
    if month == "May" or month == "October":
        discount_studio = 0.05

total_price_apartment = apartment * (1 - discount_apartment) * nights
total_price_studio = studio * (1 - discount_studio) * nights

print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")
