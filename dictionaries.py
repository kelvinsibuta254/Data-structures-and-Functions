#key: value pairs
#The key is connected with a value
#set notations used e.g {}
#keys and values enclosed in quotes

xdict = dict([("k1", "v1"), ("k2", "v2"), ("k3", "v3")])# This is a list of tuples separated by a comma
print(xdict)
print()

ydict = {"k1": "v1", "k2": "v2", "k3": "v3"}

print(ydict)
print()

#is it possible to index an element within a set? The answer is NO
#but for dictionaries the answer is YES
#for dictionaries, The keys are immutable; just like a database, when you make a database
#values are mutable

print(ydict["k1"])# key used as an index to find the value

#since the values are mutable, you can set it to something else
ydict["k1"] = 345
print(ydict)
print()

#This makes the dictionaries mutable

ydict = { 0 : "v1", 1: "v2", 2 : "v3"}# This is still a dictionary

print(ydict)
ydict[0] = 345
print(ydict)