my_first_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
my_second_list = my_first_list
my_second_list[3] = 'Z'

print("my_list_id")
print(id(my_first_list))
print(my_first_list)
print("new_list_id")
print(id(my_second_list))
print(my_second_list)

my_second_list = my_first_list[:]
my_second_list[3] = 'Z'

print(id(my_first_list))
print(my_first_list)

print(id(my_second_list))
print(my_second_list)


