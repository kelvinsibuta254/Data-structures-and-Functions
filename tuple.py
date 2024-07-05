#same as list but it is immutable i.e you can't change the values
#it is a right protected/ constant list
a = (1, 2, 3, 4, "Kayra")

print(a)
print(type(a))

print(a[0:3]) # you can do everything like slicing but you cannot change the values

#indexing also carries over
#to ensure flexibility, you can change tuple into a list e.g
a1 = list(a)
print(type(a1))
#tuple is just like a list