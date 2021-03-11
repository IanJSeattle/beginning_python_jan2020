# creating a list by hand
ag_list = ["A", "B", "C", "D", "E", "F", "G"]
new_list = ag_listpuk
new_list[2] = "Z"
print(ag_list[:])
print(new_list)

# ascii code for A is 65, the other capital letters follow
a_code = 65
number = 7

# converting ascii code into a character and storing them in a list
my_ag_list = [chr(i + a_code) for i in range(number)]