#if else
temp = int(input("Enter temperature: "))
if temp > 30:
    print("It is a hot day")
else:
    print("It is not a hot day.")

#elif
marks = int(input("Enter marks:"))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 80:
    print("Grade C")
else:
    print("Keep improving!")

#nested if
age = int(input("Enter age: "))
country = input("Enter country name: ").capitalize()

if age > 18:
    if country == "Pakistan":
        print("You can vote in Pakistan")
else:
    print("You can not vote in Pakistan")

#combined
if age > 18 and country == "Pakistan":
    print("You are an eligible voter in Pakistan")
else:
    print("You are not an eligible voter in Pakistan")

#ternary
print("Younger" if age <= 18 else "Elder")

a = 5
b = 10
max = a if a > b else b
print(max)