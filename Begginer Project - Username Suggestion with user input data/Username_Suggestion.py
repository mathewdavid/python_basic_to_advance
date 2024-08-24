#Suggested username by combining these inputs in different ways, like "firstlast123" or "last123first.

first_name = input("Enter your first name :")
last_name = input("Enter your last name :")
fav_number = input("Enter your favorite number :")

username1 = first_name + last_name + fav_number
username2 = first_name + fav_number + last_name
username3 = first_name + "123" + last_name
username4 = first_name + "_" + fav_number
username5 = last_name + fav_number
username6 = first_name + fav_number
username7 = last_name + first_name + fav_number
username8 = last_name + fav_number + first_name
username9 = last_name + "1002" + first_name
username10 = last_name + "_" + fav_number

print("\nHere are 10 username suggestions for you: ")
print("1. ", username1)
print("2. ", username2)
print("3. ", username3)
print("4. ", username4)
print("5. ", username5)
print("6. ", username6)
print("7. ", username7)
print("8. ", username8)
print("9. ", username9)
print("10. ", username10)