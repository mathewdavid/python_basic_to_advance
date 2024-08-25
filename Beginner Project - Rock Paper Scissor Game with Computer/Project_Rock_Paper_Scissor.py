import random

rock = """                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\ """

paper = """ _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_| """

scissor = """   _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\."""

game_images = [rock, paper, scissor]
user_input = int(input("What do your choose? Type 0 for ROCK, 1 for Paper or 2 for SCISSORS."))
print(f"User choose {user_input}")
print(game_images[user_input])

computer_choice = random.randint(0,2)
print(game_images[computer_choice])
print(f"Computer choose {computer_choice}")

if user_input >= 3 or user_input < 0:
    print("You typed an invalid number. You lose!")
elif user_input == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_input == 2:
    print("You lose!")
elif computer_choice > user_input:
    print("You lose!")
elif user_input > computer_choice:
    print("You win!")
elif computer_choice == user_input:
    print("It's a draw!")



