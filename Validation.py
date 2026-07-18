# 1- username must not contain more than 12 digits.
# 2- username must not contain spaces
# 3- username must not contain digits

name = input("Enter your username: ")

if len(name) > 12:
    print("Your username can't be greater than 12 characters!")
elif name.count(" ") > 0:
    print("username can't contain spaces!")
elif name.isalpha() == False:
    print("username can't contain numbers!")
else:
    print(f"Welcome {name}")