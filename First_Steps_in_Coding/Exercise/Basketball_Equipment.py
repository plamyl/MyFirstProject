annual_expanses = int(input())
shoes = annual_expanses - (annual_expanses * 0.4)
clothes = shoes - (shoes * 0.2)
ball = clothes / 4
accessories = ball / 5
total = annual_expanses + shoes + clothes + ball + accessories
print(total)

