# Write a recursive function to calculate factorial of number n.
def fact(n):
    if n==0 or n==1:
        return 1
    return fact(n-1) * n

print(fact(5))

# Write a recursive function to calculate the sum of first n natural numbers.
def sum(num):
    if num==0:
        return 0 
    return num + sum(num-1)

print(sum(5))

# Write a recursive function to print all elements in a list.
# Hint: use list & index as parameters.
numbers = [1,2,3,4,5,6]
def print_list(l, idx=0):
    if idx == len(list):
        return 
    print(list[idx])
    print_list(l, idx+1)

print(print_list(numbers))