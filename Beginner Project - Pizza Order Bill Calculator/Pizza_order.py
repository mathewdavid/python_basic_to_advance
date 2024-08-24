print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

#Pizza  Selection
pizza_amount = 0
if size == "S":
    pizza_amount += 15
elif size == "M":
    pizza_amount += 20
elif size == "L":
    pizza_amount += 25
else:
    print("Sorry you made the Wrong Choice!")

#Adding Pepperoni
if pepperoni == "Y":
    if size == "S":
        pizza_amount += 2
    else:
        pizza_amount += 3

#Adding Cheese
if extra_cheese == "Y":
    pizza_amount += 1

print(f"Your total bill of pizza : {pizza_amount}")