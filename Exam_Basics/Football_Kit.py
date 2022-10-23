shirt = float(input())
total_goal = float(input())
pants = shirt * 0.75
socks = pants * 0.20
shoes = (shirt + pants) * 2
discount = 0.15

total = shirt + pants + socks + shoes
total_after_discount = total - (total * discount)

needed_money = total_goal - total_after_discount

if total >= total_goal:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_after_discount:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f'He needs {needed_money:.2f} lv. more.')
