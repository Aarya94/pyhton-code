foods=[]
prices=[]
menu=dict(zip(foods, prices))
while True:
    if input("Do you want to add a new item to the menu? (y/n): ").lower() != "y":
        break
    food = str(input("Enter the food item: "))
    foods.append(food)
    price = float(input("Enter the price: "))
    prices.append(price)
    menu = dict(zip(foods, prices))
print("\n----- MENU -----")
for items, prices in menu.items():
    print(f"{items}: ${prices:.2f}")
    