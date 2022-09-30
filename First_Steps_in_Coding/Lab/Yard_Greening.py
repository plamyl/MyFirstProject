square_meters = float(input())
price_per_sqm = 7.61
total_price = square_meters * price_per_sqm
discount = 0.18
final_discount = total_price * discount
final_price = total_price - final_discount
print(f"The final price is: {final_price} lv.")
print(f"The discount is: {final_discount} lv.")
