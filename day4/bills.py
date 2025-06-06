import random


friends = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

# random_int = random.randint(0, len(friends) - 1)
# random_friend = friends[random_int]
# print(f"{random_friend} is going to buy the meal today!")

print(f"{random.choice(friends)} is going to buy the meal today!")

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])