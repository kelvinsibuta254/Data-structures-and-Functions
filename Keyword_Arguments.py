def user_info(name= str, age=None):
    """Prints user information."""
    print(f"Name: {name}")
    if age:
        print(f"Age: {age}")
user_info(name="Bob", age=30)