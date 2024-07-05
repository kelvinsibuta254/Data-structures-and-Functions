#Deletes elements from a list
my_list = [10, 20, 30, 40, 50]
new_list = my_list.remove(30)
print(new_list)#prints only four items

my_list = [10, 20, 30, 40, 50]
new_list2 = my_list.remove(my_list[0])
print(new_list2)