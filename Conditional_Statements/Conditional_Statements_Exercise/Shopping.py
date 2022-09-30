budget = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())

price_video_cards = 250 * video_cards
price_processors = (0.35 * price_video_cards) * processors
price_ram = (0.10 * price_video_cards) * ram

total = price_ram + price_processors + price_video_cards

if video_cards > processors:
    total -= total * 0.15
diff = abs(budget - total)
if budget >= total:
     print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")


