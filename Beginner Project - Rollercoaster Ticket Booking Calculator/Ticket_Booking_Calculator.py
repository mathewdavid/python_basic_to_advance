# Ticket Booking System
print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
bill = 0

#elif age >=45 or age <= 55:
#bill = 0
#print(f"Mid Life tickets are {bill}")

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age<=12:
        bill = 5
        print(f"Child tickets are {bill}")
    elif age<=18:
        bill = 7
        print(f"Youth tickets are {bill}")
    elif age >= 45 and age <= 55:
        bill = 0
        print(f"Everything will be fine. Have a free ride on us {bill}")
    else:
        bill = 12
        print(f"Adult tickets are {bill}")

    wants_photo = input("Do you want to have a photo to be taken? Type y for YES and n for NO. :")
    if wants_photo == "y" or wants_photo == "Y":
        total_bill = bill + 3
        print(f"Your total bill is {total_bill}")
    else:
        print(f"Your total bill is {bill}")

else:
    print("Sorry, You can't ride")