groceries = [('beans', 1.35),
             ('lettuce', 1),
             ('macaroni', 2.95),
             ('cheese', 8.99)]

total = 0
for item in groceries:
    name = item[0]
    price = item[1]
    print(name)
    total += price

total = '{:.2f}'.format(total)
print(f'${total} spent')
