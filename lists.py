#Slicing: allows you to extract sub-lists from a list using start, stop, and step indices
#use the syntax, list[start:stop:step]
#start index is inclusive, stop index is exclusive, step index is the interval between elements
my_list = [10, 20, 30, 40, 50]
slice = my_list[1:4]
print(slice)#prints slice

slice2 = my_list[::2] #step of 2
print(slice2)

slice3 = my_list[::-1] #reverses the list
print(slice3)
