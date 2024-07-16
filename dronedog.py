"""
"""
print("Welcome to Drone Dogs")
print("1 Hotdog")
print("2 Hotdogs")
print("3 Hotdogs")

num_choice = int(input("How many Hotdogs would you like?:"))
while num_choice < 1 or num_choice > 3:
    num_choice = int(input("Not a valid choice: "))

print("""
Choose your condiment:
[1] Relish
[2] Ketchup
[3] Mustard
[4] Plain
""")
choice = input("")
if choice == "1" :
   print("You chose to put Relish on your Hotdog")
elif choice == "2" :
   print("You chose to put Ketchup on your Hotdog")
elif choice == "3" :
   print("You chose to put Mustard on your Hotdog")
elif choice == "4" :
   print("You chose to put no condiments on your Hotdog")

chosenToppings = []
while True:
    toppingCount = int(input('How many toppings would you like?: '))
    if toppingCount <= 3:
        for i in range(1,toppingCount+1):
            top = 1
            while top in [1,2,3]:
                top = int(input('Enter choice 1-3: '))
                topping.append(top)
            break
            break
        else:print('Enter a number less than three please')
chosenToppings = [ "[1]tomato", "[2]lettuce", "[3]pickles", "[4]cheese", "[5]onions" ]
