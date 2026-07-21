# Print multipication table of number n
num = int(input("Enter a number: "))

i = 1
while i<=10:
    print(f"{num} * {i} = {num*i}")
    i+=1 

# Print the elements of the following list using loop
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
j = 0
while j < len(list):
    print(list[j])
    j+=1

# Search for a num x in this tuple using loop
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter a number: "))
k = 0
while k < len(tup):
    if x == tup[k]:
        print("Found at index ", k)
        break
    else:
        print("finding...")
    k+=1