num1 = float(input("Enter first numer: "))
num2 = float(input("Enter second numer: "))
op = input("Choose operation(+ - * / %): ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    #if num2 > 0:
    print(round(num1 / num2, 2))
elif op == "%":
    print(num1 % num2)
else:
    print(f"{op} is not a valid operator!")