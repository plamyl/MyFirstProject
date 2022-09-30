flowers = input()
amount = int(input())
budget = int(input())
total = 0

if flowers == 'Roses':
    total = amount * 5
    if amount > 80:
        total = total - (total * 0.10)
elif flowers == 'Dahlias':
    total = amount * 3.80
    if amount > 90:
        total = total - (total * 0.15)
elif flowers == 'Tulips':
    total = amount * 2.80
    if amount > 80:
        total = total - (total * 0.15)
elif flowers == 'Narcissus':
    total = amount * 3
    if amount < 120:
        total = total + (total * 0.15)
elif flowers == 'Gladiolus':
    total = amount * 2.50
    if amount < 80:
        total = total + (total * 0.20)

if total <= budget:
    money_left = budget - total
    print(f"Hey, you have a great garden with {amount} {flowers} and {money_left:.2f} leva left.")
else:
    money_needed = total - budget
    print(f"Not enough money, you need {money_needed:.2f} leva more.")


