import random

words = ["anaconda", "vincenzo", "wikipedia", "horror", "stubborn"]

hangman = {0: ("   ",
               "   ",
               "   "),
           1: (" o ",
               "   ",
               "   "),
           2: (" o ",
               " | ",
               "   "),
           3: (" o ",
               "/| ",
               "   "),
           4: (" o ",
               "/|\\",
               "   "),
           5: (" o ",
               "/|\\",
               "/  "),
           6: (" o ",
               "/|\\",
               "/ \\")}

def display_hangman(wrong_guesses):
    print("*************")
    print("   HANGMAN   ")
    print("*************")
    for line in hangman[wrong_guesses]:
        print("    ", line)
    print("*************")

def display_hint(hint):
    print("WORD TO GUESS")
    print(" ".join(hint))
    print("*************")

def answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = len(answer) * ["_"]
    wrong_guesses = 0
    guessed_letters = set()
    isrunning = True

    while isrunning:
        display_hangman(wrong_guesses)
        display_hint(hint)
        guess = input("\nGuess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Enter valid input!")
            continue
        if guess in guessed_letters:
            print(f"{guess} already guessed!")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_hangman(wrong_guesses)
            print("--YOU WIN!--")
            print(f"Word = {answer}")
            print("*************")
            isrunning = False

        elif wrong_guesses >= 6:
            display_hangman(wrong_guesses)
            print("--YOU LOST!--")
            print(f"Word = {answer}")
            print("*************")
            isrunning = False
    
if __name__ == '__main__':
    main()