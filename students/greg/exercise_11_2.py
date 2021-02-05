names = ['matt', 'greg', 'john', 'tom', 'harry']

'''
for num, value in enumerate(names):
    print(num, value)
'''

new_names = [f'{num} {value}' for num, value in enumerate(names, start=1)]

print(new_names)

