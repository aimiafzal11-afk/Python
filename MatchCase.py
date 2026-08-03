def week_day(day):
    match day:
        case 1:
            print("It's Monday!")
        case 2:
            print("It's Tuesday")
        case 3:
            print("It's Wednesday!")
        case 4:
            print("It's Thursday!")
        case 5:
            print("It's Friday!")
        case 6:
            print("It's Saturday!")
        case 7:
            print("It's Sunday!")
        case _:
            print("Invalid input!")

week_day(3)

def is_weekend(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            print("It's not a weekend")
        case "Saturday" | "Sunaday":
            print("It's a weekend")
        case _:
            print("Invalid input!")

is_weekend("Friday")