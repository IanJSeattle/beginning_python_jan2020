my_list = ['robert', 'dash', 'daniel', 'jake']

rank_list = [f'{num+1} {name.title()}' for num, name in enumerate(my_list)]

for rank_name in rank_list:
    print(rank_name)
