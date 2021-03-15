budget = float(input())
season = input()

amount_spent = 0
destination = ""
place_for_vacation = ""

if budget <= 100 and season == "summer":
    destination = "Bulgaria"
    place_for_vacation = "Camp"
    amount_spent = budget * 0.3
elif budget <= 100 and season == "winter":
    destination = "Bulgaria"
    place_for_vacation = "Hotel"
    amount_spent = budget * 0.7
elif budget <= 1000 and season == "summer":
    destination = "Balkans"
    place_for_vacation = "Camp"
    amount_spent = budget * 0.4
elif budget <= 1000 and season == "winter":
    destination = "Balkans"
    place_for_vacation = "Hotel"
    amount_spent = budget * 0.8
else:
    destination = "Europe"
    place_for_vacation = "Hotel"
    amount_spent = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{place_for_vacation} - {amount_spent:.2f}")
