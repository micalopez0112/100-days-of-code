enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    
    print(f"enemies inside function: {enemies}")
    
print(f"enemies outside function: {enemies}")

##################


def drink_potion():
    potion_strength = 2
    print("You drink a potion.")
    return

drink_potion()
# print(potion_strength)

#####################

game_level = 3 #10
aliens = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_alien = aliens[0]
    print(f"First alien is: {new_alien}")
    
print(new_alien)