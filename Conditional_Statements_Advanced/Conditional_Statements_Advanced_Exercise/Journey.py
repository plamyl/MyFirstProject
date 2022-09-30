budget = float(input())
season = input()
destination = ''
type_of_vacation = ""
total = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        type_of_vacation = 'Camp'
        total = budget * 0.3
    elif season == 'winter':
        type_of_vacation = 'Hotel'
        total = budget * 0.7

elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        type_of_vacation = 'Camp'
        total = budget * 0.4
    elif season == 'winter':
        type_of_vacation = 'Hotel'
        total = budget * 0.8
else:
    destination = 'Europe'
    type_of_vacation = 'Hotel'
    total = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{type_of_vacation} - {total:.2f}")

