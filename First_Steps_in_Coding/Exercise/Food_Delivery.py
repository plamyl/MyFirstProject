chicken_menu = 10.35
fish_menu = 12.40
veggie_menu = 8.15

number_of_chicken_menu = int(input())
number_of_fish_menu = int(input())
number_of_veggie_menu = int(input())

total = chicken_menu * number_of_chicken_menu + fish_menu * number_of_fish_menu + veggie_menu * number_of_veggie_menu
desert = total * 0.2

total += desert + 2.5
print(total)