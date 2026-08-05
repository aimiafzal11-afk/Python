import random

dice_set = {1 : ("┌─────────┐",
                 "│         │",
                 "│    ●    │",
                 "│         │",
                 "└─────────┘"),
            2 : ("┌─────────┐",
                 "│  ●      │",
                 "│         │",
                 "│      ●  │",
                 "└─────────┘"),
            3 : ("┌─────────┐",
                 "│  ●      │",
                 "│    ●    │",
                 "│      ●  │",
                 "└─────────┘"),
            4 : ("┌─────────┐",
                 "│  ●   ●  │",
                 "│         │",
                 "│  ●   ●  │",
                 "└─────────┘"),
            5 : ("┌─────────┐",
                 "│  ●   ●  │",
                 "│    ●    │",
                 "│  ●   ●  │",
                 "└─────────┘"),
            6 : ("┌─────────┐",
                 "│  ●   ●  │",
                 "│  ●   ●  │",
                 "│  ●   ●  │",
                 "└─────────┘"),}

noOfDice = int(input("How many dices? "))
dice = []
total = 0

for die in range(noOfDice):
    dice.append(random.randint(1, 6))

for die in range(noOfDice):
    for line in dice_set.get(dice[die]):
        print(line)

for die in dice:
    total += die
print(f"Total: {total}")