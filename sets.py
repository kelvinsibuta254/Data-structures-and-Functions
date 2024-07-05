#intesection is the overlap between two sets; its like the bollean AND
#union() is like OR in bollean algebra
# sets are unordered, meaning you can't index the elements the way that you would with a list or tuple; they are mutable
# uses carly brackets
# can only keep unique elements
a = {3, 4, 5, 6, 7}
print(a)
print(type(a))

# can only keep unique elements
a = {3, 4, 5, 6, 7, 7, 7}
print(a)

#You can create an empty set
b = set()
print(b)
#sets doesn't allow duplicates