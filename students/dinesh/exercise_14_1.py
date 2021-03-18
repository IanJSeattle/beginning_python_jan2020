item_price = [('chicken', 2.99), ('shrimp', 4.99), ('lamb', 6.99), ('steak', 4.99)]
total = 0
for item in item_price:
    name = item[0]
    price = item[1]
    print(name)
    total += price

print(f'{total} spent')