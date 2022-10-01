days = int(input())
room_type = input()
rating = input()
total = 0
price = 0
discount = 0

if room_type == 'room for one person':
    price = 18
elif room_type == 'apartment':
    price = 25
    if days < 10:
        discount = 0.3
    elif 10 <= days <= 15:
        discount = 0.35
    else:
        discount = 0.5

elif room_type == 'president apartment':
    price = 35
    if days < 10:
        discount = 0.10
    elif 10 <= days <= 15:
        discount = 0.15
    else:
        discount = 0.20

total = (days - 1) * price
total = total - (total * discount)

if rating == 'positive':
    total = total + (total * 0.25)
elif rating == 'negative':
    total = total - (total * 0.10)
print(f'{total:.2f}')
