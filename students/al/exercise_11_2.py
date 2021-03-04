names = ("John", "Mary", "Jim", "Dana")
print (names)
[ "1 John", "2 Mary", "3 Jim", "4 Dana"]
for name in names:
    print (name)
for num, name in enumerate(names):
    print(f'Name number {num+1} is {name.title()}')
    print(f'Your name is {name}.')