names = ['John', 'Vinay', 'Ram', 'Mark']
rankList = [f'{num+1} {name.title()}' for num, name in enumerate(names)]
for x in rankList:
    print(x)

