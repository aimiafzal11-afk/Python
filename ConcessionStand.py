menu = {"popcorn" : 2,
        "hotdog" : 3,
        "pizza" : 3,
        "drink" : 1.5,
        "jelly" : 1,
        "chips" : 2,
        "chocolate" : 3.5,
        "burger" : 2.25}

cart = []
total = 0

print("---------MENU----------")
for key, value in menu.items():
    print(f"{key:10} : {value:.2f}$")
print("-----------------------")

while True:
    item = input("Select items to buy(q to quit): ").lower()
    if item == "q":
        break
    elif menu.get(item) is not None:
        cart.append(item)

print("\n------YOUR CART------")
for item in cart:
    print(item, end = " ")
    total += menu.get(item)
print(f"\nTOTAL PRICE = {total}$")
