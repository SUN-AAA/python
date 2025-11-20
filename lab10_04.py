menu = {"Americano" : "3,000 won",
        "Ice Americano" : "3,500 won",
        "Cappuccino" : "4,000 won",
        "Cafe Latte" : "4,500 won",
        "Espresso" : "3,600 won"}

for key in menu:
    print(f"{key}\tPrice: {menu[key]}")

order = input("Please select one of the menus above: ")
if order in menu.keys():
    print(f"{order} is {menu[order]}. Please pay.")
else:
    print(f"Sorrry, {order} is not in the menu")
