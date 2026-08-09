import random

def spin_row():
    row = ['🍭', '🎶', '⭐', '🍒', '🌸']
    return [random.choice(row) for _ in range(3)]

def print_row(row):   
    print(" | ".join(row))

def get_payout(row):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍭':
            return 3
        elif row[0] == '🎶':
            return 5
        elif row[0] == '⭐':
            return 10
        elif row[0] == '🍒':
            return 15
        elif row[0] == '🌸':
            return 20
    return 0
        
def main():
    balance = 100

    print("**********************")
    print("     SLOT MACHINE     ")
    print("**********************")
    while True:
        print("----------------------")
        print(f"Current Balance: ${balance}")
        bet = input("Enter amount to bet: $")
        print("Spinning...\n")
        if not bet.isdigit():
            print("Invalid input!")
            continue

        bet = int(bet)
        if bet <= 0 or bet > balance:
            print("Please enter the valid amount! ")
        else:
            balance -= bet

        row = spin_row()
        print_row(row)

        payout = get_payout(row)
        if not payout == 0:
            print(f"YOU WON ${payout}")
            balance += payout           
        else:
            print("YOU LOSE THIS BET!")
        print(f"YOUR BALANCE NOW: ${balance}")

        play_again = input("Want to play again (Y/N)? ").upper()
        if not play_again == 'Y':
            break

    print("-----------------------")
    print("  THANKS FOR PLAYING!  ")
    print("-----------------------")

if __name__ == '__main__':
    main()