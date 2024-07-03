z = dict()
z["a"] = "alpha"
z["g"] = "gamma"
z["o"] = "omega"

## {"a" : "alpha", "o" : "omega", "g" : "gamma"}

#elements of the set are the keys not values
#Simple lookup returns "alpha"
print(z["a"])
z["a"] = 6 #put the key value into dict
print("a" in z) #True: for a set, this is in respect to a key not a value i.e is a in z?
#print values
if "z" in z:
    print(z["z"]) #print the value if the key is in the set
if "a" in z:
    print(z["a"])

#is this key in that dictionary?

#use try except to raise an error alarm if the key is not present in a dictionary (Keyerror)

# when converting a dictionary to a set, python is not going to extract values as the elements but as as keys
#because sets are only allowed to have singular elements