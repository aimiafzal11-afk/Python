#WAF to print the length of a list. (list is the parameter)
def print_length(list):
    print(len(list))

l = [1,2,3,4,6,7]
print_length(l)

#WAF to print the elements of a list in a single line. (list is the parameter)
def print_el(list):
    for el in list:
        print(el, end = " ")

print_el(l)

#WAF to find the factorial of n. (n is the parameter)
def fact(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial

print(f"\nFactorial = {fact(5)}")