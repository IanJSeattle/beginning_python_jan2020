my_list = ['joe', 'dan', 'ian', 'tim']
rank_list = [f'{num+1} {name.title()}' for num, name in enumerate(my_list)]
print(rank_list)