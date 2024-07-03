a = {3, 4, 5}
b = {4, 5, 6, 7, 8 , 9, 6, 6, 5, 4}
print(b)
c = a.intersection(b)
print(c)
d = a.union(b)
print(d)
e = 8
print(e in b)
print(e in a)
f = b.difference(a)
print(f)


x = {3, 4, 5, 6}
y = {5, 4, 3, 6}
print(x==y)

c = [3, 4, 5, 6, 6, 7, 7, 8, 8]
print(c)
d = set(c)
print(d)
e = list(d)
print(e)

#sets can help remove duplicates or repetitions from a list and other data structures
#You can call a unique function in a high level language using a nested loop
# use keys to index your elements within your set
