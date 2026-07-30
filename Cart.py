foods = []
prices = []
total = 0

while True:
    food = input("Enter food item (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input("Enter price of the food item: $"))
        foods.append(food)
        prices.append(price)

print("--- YOUR CART ---")
for food in foods:
    if food == foods[-1]:
        print(food)
    else:
        print(food, end = ", ")
for price in prices:
    total += price
print("Total price of food = $", total)