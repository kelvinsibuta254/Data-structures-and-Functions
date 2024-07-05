count = 0 #Global variable
def increment():
    count += 1 #This refers to the local count within the function
    print(count) #prints a local variable
    increment()
print(count)#Output: 0 (Global count remais unchanged)