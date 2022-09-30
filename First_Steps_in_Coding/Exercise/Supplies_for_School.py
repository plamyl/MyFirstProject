pens = int(input())
markers = int(input())
detergent = int(input())
discount = int(input())

price_per_pens = pens * 5.80
price_per_markers = markers * 7.20
price_per_detergent = detergent * 1.20

total = price_per_detergent + price_per_markers + price_per_pens
total_after_discount = total - (total * (discount/100))
print(total_after_discount)
