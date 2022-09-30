length = int(input())
width = int(input())
height = int(input())
taken_volume = float(input())

aquarium_volume = length * width * height
volume_in_liters = aquarium_volume * 0.001
taken_volume_in_percent = taken_volume / 100
needed_liters = volume_in_liters * (1 - taken_volume_in_percent)
print(needed_liters)

