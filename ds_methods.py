#Lists are Dynamic arrays, order matters, frequent insertions and deletions
"""Lists methods:
append (item) - add item to the end of a list
remove(item) - Removes first occurence of item
sort() - Sort the list in ascending order
pop(index) - Remove and return item at index
"""
# my_list = [1, 2, 3]
# my_list.append(0)
# print(my_list)


# my_list = [1, 2, 3, 2]
# my_list.remove(3)
# print(my_list)


# my_list = [3, 1, 4, 2]
# my_list.sort() #: only accepts numbers
# print(my_list)


# my_list = [3, 1, 4, 2]
# item = my_list.pop(2) #pop removes an item at index 2
# print(item)
# print(my_list)

#Dictionaries
#Use Cases: Fast lookups by key, unordered data

#Common Methods
"""keys(): Return all keys
values(): Return all values
items(): Return all key-value pairs
get(key): Return value for key
"""

# my_dict = {"a" : 1, "b" : 2, "c" : 3}
# print(my_dict.keys())
# print(my_dict)
# print(my_dict["b"]) #prints a value associated with key ["b"]

# dict = {"a" : 1, "b" : 2, "c" : 3}
# print(dict.values())
# print(dict)
# print(dict["b"])

# dict["a"] = 90# replaces the value at key "a"

# dictionary = {"a" : 1, "b" : 2, "c" : 3}
# print(dictionary.items()) #print keys and values



# dict = {"a" : 1, "b" : 2, "c" : 3}
# print(dict.get("c"))# access the value associated with key "c"
#N/B: key for keys, get for values

"""
Set Methods:
    add(item): Add item to the set
    remove(item): Remove item from the set
    union(set): Return union of sets
    intersection(set): Return a new set that contains only the elements that are present in both"""

# my_set = {1, 2, 3, 4}
# my_set.add(2)
# print(my_set)


# my_set = {1, 2, 3, 4}
# my_set.remove(2)
# print(my_set)

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# union_set = set2.union(set1)
# print(union_set)



# set1 = {1, 3, 7, 5}
# set2 = {3, 4, 5, 4, 3}

# intersection_set = set2.intersection(set1)
# print(intersection_set)# prints out common values in both sets

#Set cannot allow duplicates that's why there's only one 3
#Use Cases: Unique items, membership tests, set operations


"""Tuple
Used for fixed collections
Ensures immutability
Common Methods
count(item): Return number of occurrences of item
index(item): Return first index item
"""

# my_tuple = (1, 2, 3, 2, 4, 2)
# count = my_tuple.count(2)#counts the number of times 2 occurs
# print(count)

my_tuple = (1, 2, 3, 2, 4, 2)
index = my_tuple.index(3)
print(index)