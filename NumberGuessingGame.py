import random

low = 1
high = 100
num = random.randint(low, high)
guess = 0

while True:
    userNo = input(f"Guess the number b/w {low} and {high}: ")
    if userNo.isdigit():
        userNo = int(userNo)
        guess += 1
        if userNo > num:
            print("TOO HIGH! Try Again")
        elif userNo < num:
            print("TOO LOW! Try Again")
        elif userNo == num:
            print("-----------------")
            print("CORRECT!")
            print(f"The number is {num}")
            print("-----------------")
            break
    else:
        print("Invalid input!")
        print(f"Please select a number b/w {low} and {high}")

print(f"NUMBER OF GUESSES TAKEN = {guess}")
print("-----------------")