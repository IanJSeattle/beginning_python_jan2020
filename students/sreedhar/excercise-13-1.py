str1 = 'Hello World'
slice1 = str1[:5]
slice2= str1[6:]
slice3= slice1[::-1]+' '+slice2[::-1]
print(slice1)
print(slice2)
print(slice3)

list1 = ["a", "b", "c", "d", "e", "f", "g", "h","i"]
print(list1[2:7:1])