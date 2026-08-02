questions = ("1. OOP main pillars?",
             "2. Polymorphism types?",
             "3. Basic Inheritance types?")
options = (("A. 2" , "B. 3" , "C. 4"),
           ("A. 1" , "B. 2" , "C. 3"),
           ("A. 2" , "B. 3" , "C. 4"))
answers = ("C", "B", "B")

q_no = 0
guesses = []
score = 0
for q in questions:
    print("--------------------------")
    print(q)
    for option in options[q_no]:
        print(option)

    guess = input("Choose (A, B, C): ").upper()
    guesses.append(guess)

    if guess == answers[q_no]:
        print("CORRECT!")
        score += 1
    else:
        print("INCORRECT!")
        print(f"The correct answer is {answers[q_no]}")
    q_no+=1

print("-----------------------")
print("        RESULTS        ")
print("-----------------------")

print("answers", end = " ")
for answer in answers:
    print(answer, end = " ")
print()

print("guesses", end = " ")
for guess in guesses:
    print(guess, end = " ")
print()

print(f"YOUR SCORE IS {score}/3!")