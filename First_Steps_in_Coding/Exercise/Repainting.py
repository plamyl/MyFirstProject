nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

price_for_naylon = (nylon + 2) * 1.50
price_for_paint = (paint * 1.1) * 14.50
price_per_thinner = thinner * 5.00

total_of_materials = price_per_thinner + price_for_paint + price_for_naylon + 0.40
workers_payment = (total_of_materials * 0.3) * hours

total = total_of_materials + workers_payment
print(total)

