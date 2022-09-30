pages = int(input())
pages_per_hour = int(input())
days_per_book = int(input())

total_hours = int(pages / pages_per_hour)
total_hours_per_day = int(total_hours / days_per_book)

print(total_hours_per_day)