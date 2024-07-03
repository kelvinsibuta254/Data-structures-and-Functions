z = dict()
z["a"] = "alpha"
z["g"] = "gamma"
z["o"] = "omega"

## {"a" : "alpha", "o" : "omega", "g" : "gamma"}

#elements of the set are the keys not values
#Simple lookup returns "alpha"
print(z["a"])
print(set(z))

# when converting a dictionary to a set, python is not going to extract values as the elements but as as keys
#because sets are only allowed to have singular elements