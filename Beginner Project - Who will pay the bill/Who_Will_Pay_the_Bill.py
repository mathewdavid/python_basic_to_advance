import random

friend = ["Mayur","Ankur","Disha","Manisha","Sidharth"]

# 1st Option
random_friend = random.choice(friend)
print(random_friend)

# 2nd Option
random_index = random.randint(0,4)
print(friend[random_index])