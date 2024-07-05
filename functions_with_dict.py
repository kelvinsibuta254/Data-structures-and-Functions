def funcd(d, v): #takes a dictionary as a parameter (input)
    for key in d: #iterate/ search through all the keys in the dictionary d, this is a set operator
        if d[key] == v: #if the dictionary element associated with that key is equal to the value (key is acting as an index)

            return dict()#return an empty dict if the key is not their for that given value
        
ydict = dict([("v1", 1), ("v2", 2), ("v3", 3)])
print(ydict)

print(funcd(ydict, 2))#prints
print(funcd(ydict, 7)) # get an empty dict if 7 isn't fount

