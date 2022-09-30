deposit_sum = float(input())
deposit_term = int(input())
interest_rate = float(input())

interest_per_year = deposit_sum * (interest_rate / 100)
interest_per_month = interest_per_year / 12
total = deposit_sum + (deposit_term * interest_per_month)
print(total)