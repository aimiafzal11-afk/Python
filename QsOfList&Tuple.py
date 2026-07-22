#Ask the user to enter names of 3 fav movies and store them in a list
n1 = input("Enter your 1st fav movie name: ")
n2 = input("Enter your 2nd fav movie name: ")
n3 = input("Enter your 3rd fav movie name: ")

l1 = [n1, n2, n3]
print(l1) 

#Check whether the list contains palindrome of elements.
l2 = [1, 2, 3, 2, 1]

pal = l2 == l2[::-1]
if pal == True:
    print(f"List {l2} contains a palindrome of elements.")
else:
    print(f"List {l2} does not contain a palindrome of elements.")

#Count the number of students with the "A" grade in the following tuple("C", "D", "A", "А", "В", "B", "A")
grades = ("C", "D", "A", "A", "B", "B", "A")
count = grades.count("A")
print(f"There are {count} students with the A grade.")

#Store the above values in a list & sort them from "A" to "D".
list = ["C", "D", "A", "A", "B", "B", "A"]
list.sort()
print(list)