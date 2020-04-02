"""
CP1404/CP5632 - Practical - Suggested Solution
Shop calculator program to determine total (discounted) price
"""

total = 0
items = int(input("Enter the number of items:"))
for i in range(items):
    price = float(input("Enter the price:"))
    total += price

if total > 100:
    total *= 0.9
    print(total)



