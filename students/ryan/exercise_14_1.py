grocery_receipt = [('bread', 1.99), ('water', 0.75), ('chips', 3.49), ('apples', 0.95)]

total = 0
for item in grocery_receipt:
	print(item[0])
	total += item[1]

total = '{:.2f}'.format(total)
print(f'${total}')
