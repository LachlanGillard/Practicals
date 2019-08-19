price = 0
total_price = 0
items = int(input("welcome, how many item are you buying: "))
while items <= 0:
    print("Please choose an amount larger then 0")
    items = int(input("welcome, how many item are you buying: "))

for i in range(items):
    price = float(input("Price of item: "))
    total_price += price
if total_price > 100:
    total_price *= 0.1

print("Total price for", items, "is: $ {:.2f}".format(total_price))
