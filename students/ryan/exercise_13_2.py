a_code = 65
number = 7

print("Copying a list without a slice")
print("------------------------------")
my_list = [chr(i + a_code) for i in range(number)]

new_list = my_list
new_list[3] = 'Z'

print("my_list id")
print(id(my_list))
print(my_list)
print("new_list id")
print(id(new_list))
print(new_list)

print("\n")
print("Copying a list with a slice")
print("---------------------------")
my_list = [chr(i + a_code) for i in range(number)]

new_list = my_list[:]
new_list[3] = 'Z'

print("my_list id")
print(id(my_list))
print(my_list)
print("new_list id")
print(id(new_list))
print(new_list)
