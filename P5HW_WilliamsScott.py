# Scott Williams
# 7/14/2025
# P5HW
# Using Python functions to create a highly questionable adventure game

#import the random python library to utilize in 'damage' based dice rolls
import random


#function to house the starting stats of our character, and return updated values for those variables
def createFrank():
    #Create variables for the dictionary
    name = "Frank"
    health_points = 100
    power = 50
    inventory = []
    gold = 0
    
    #Choose to start with potions, via a while loop that persists until 'n' is entered
    add_item = input(f"Should {name} have any items to begin? (y/n): ")
    while add_item.lower() != "n":
        obj = input("Enter an item to add to inventory (health potion / mana potion): ").lower()
        if obj in ["health potion", "mana potion"]:
            inventory.append(obj)
        else:
            print("Only 'health potion' or 'mana potion' are allowed.")
        print()
        add_item = input("Add another item? (y/n): ")

    print(f"\nYou successfully created {name}'s inventory:")
    print(inventory)
    print()

    #Dictionary that can be updated during each event
    character = {
        "name": name,
        "inventory": inventory,
        "health_points": health_points,
        "power": power,
        "gold": gold
    }
    return character




#our main function that contains all core components of the game's encounters and victory settings
def main():
    #introduction
    print("Welcome to Frank's Adventure! What is the adventure?  Murder!")
    print("Today, Frank saw an advertisement on TV for a new vacation theme park named Tatertown.  The cost?  200 golden coins.")
    print("Full of enthusiasm to visit the theme park, but unfortunately lacking funds, he has decided to pay for this trip the only way he knows how:")
    print("By beating up small, defenseless wildlife creatures and taking their coins for himself.  Also, Frank can cast wizard spells.")
    print("Adventure awaits!")
    character = createFrank()

    #prompt to select our destination to fight enemies for gold
    while character["gold"] < 200 and character["health_points"] > 0:
        print("Where would you like to go?")
        print("1. Forest ")
        print("2. Meadow ")
        print("3. Pond ")
        print(f"Current Gold: {character['gold']}")
        choice = input("Enter 1, 2, or 3: ")

        #if/else statement to determine location and avoid errors if input is invalid.  also contains enemy hp, damage range, and gold dropped
        print()
        if choice == "1":
            encounter(character, "extremely violent squirrel", 20, (2, 6), 10)
        elif choice == "2":
            encounter(character, "aggressive, bloodthirsty small ferret", 30, (5, 10), 20)
        elif choice == "3":
            encounter(character, "enraged, roided out capybara", 40, (8, 15), 50)
        else:
            print("Invalid location. Choose again.\n")

        if character["health_points"] <= 0:
            print("Game over. Frank was killed and it is fair to say he deserved this.")
            return

    
    final_encounter(character)

#function for the game's combat loop
def encounter(character, enemy_name, enemy_health, damage_range, gold_reward):
    print(f"You have encountered an {enemy_name}!\n")

    #while loop that will cause the combat to continue until Frank's (or the enemy's) health reaches 0
    while enemy_health > 0 and character["health_points"] > 0:
        print(f"{enemy_name}'s health: {enemy_health}")
        print(f"{character['name']}'s HP: {character['health_points']} | Power: {character['power']}")
        print("What will you do?")
        print("1. Use ability")
        print("2. Use potion")

        action = input("Enter 1 or 2: ")
        print()

        #if/else block to consume the turn if an improper input is detected
        if action == "1":
            damage = use_ability(character)
        elif action == "2":
            use_potion(character)
            damage = 0
        else:
            print("Invalid choice. Turn wasted.")
            damage = 0

        enemy_health -= damage

        #if statement that provides rewards once the enemy's hp reaches 0
        if enemy_health <= 0:
            print(f"You defeated the {enemy_name}!  You are the best!\n")
            potion = random.choice(["health potion", "mana potion"])
            character["inventory"].append(potion)
            character["gold"] += gold_reward
            print(f"The {enemy_name} dropped a {potion} and {gold_reward} gold!\n")
            return

        #enemy attack text and damage feedback
        counter_damage = random.randint(*damage_range)
        character["health_points"] -= counter_damage
        print(f"The {enemy_name} attacks! {character['name']} loses {counter_damage} HP.")
        print(f"{character['name']}'s health is now {character['health_points']}\n")

        #if statement to provide the gameover prompt if hp reaches 0
        if character["health_points"] <= 0:
            print(f"{character['name']} has been defeated by the {enemy_name}...\n")
            return

#function for Frank's abilities and what they do
def use_ability(character):

    print("Choose an ability:")
    print("1. fight (Deals 1–5 damage, no power cost)")
    print("2. fireball (Deals 5–15 damage, costs 5 power)")
    print("3. lightning bolt (Deals 30 damage, costs 25 power)")

    choice = input("Enter ability number (1–3): ")

    if choice == "1" or choice.lower() == "fight":
        damage = random.randint(1, 5)
        print(f"{character['name']} uses fight and deals {damage} damage!")
        return damage

    #if/else blocks to utilize current power in order to determine if a sufficient amount is available to cast
    
    elif choice == "2" or choice.lower() == "fireball":
        if character["power"] >= 5:
            damage = random.randint(5, 15)
            character["power"] -= 5
            print(f"{character['name']} uses fireball and deals {damage} damage!")
            print(f"{character['name']} now has {character['power']} power left.")
            return damage
        else:
            print("Not enough power to use fireball!")
            return 0

    elif choice == "3" or choice.lower() == "lightning bolt":
        if character["power"] >= 25:
            character["power"] -= 25
            damage = 30
            print(f"{character['name']} uses lightning bolt and deals {damage} damage!")
            print(f"{character['name']} now has {character['power']} power left.")
            return damage
        else:
            print("Not enough power to use lightning bolt!")
            return 0

    #else statement that burns the turn if an improper command is entered
    else:
        print("Invalid ability. Turn wasted!")
        return 0

#function to use the potions obtained in the game
def use_potion(character):
    potions = [item for item in character["inventory"] if item in ["health potion", "mana potion"]]

    if not potions:
        print("You have no potions to use.\n")
        return

    print("Choose a potion:")
    print("1. health potion (+50 HP)")
    print("2. mana potion (+50 Power)")
    print(f"Inventory: {character['inventory']}")
    choice = input("Enter 1 or 2: ")

    #if/else block to use a health potion (if you have one) and to return the health in the dictionary's variable
    if choice == "1":
        if "health potion" in character["inventory"]:
            character["health_points"] += 50
            character["inventory"].remove("health potion")
            print(f"{character['name']} used a health potion and restored 50 health points.\n")
        else:
            print("You don't have a health potion.\n")

    #if/else block to use a mana potion (if you have one) and to return the power in the dictionary's variable
    elif choice == "2":
        if "mana potion" in character["inventory"]:
            character["power"] += 50
            character["inventory"].remove("mana potion")
            print(f"{character['name']} used a mana potion and restored 50 power.\n")
        else:
            print("You don't have a mana potion.\n")

    else:
        print("Invalid choice. Turn wasted.\n")
    

#function for the final encounter, prompted by reaching 200 gold.  made this a separate function from main initially for troubleshooting as I decided late to add this encounter after all the other code was done
#also wanted flavor text specific to this encounter so it was simpler to isolate it than to rework the previous functions to incorporate the duck specific prompts
def final_encounter(character):
    print("Frank finally has enough gold to afford the trip to Tatertown, but as he gleefully counts his spoils, the sky darkens, and the ground quakes.")
    print("The hair on the back of Frank's neck stands up as he feels an ominous presence closing in from seemingly all directions, stomping closer and closer and closer...")
    print("Until finally, Frank hears a little 'quack' behind him.  Spinning around, he locks eyes with his final opponent.")
    print("Before Frank stands nature's chosen avatar, sent to exact vengeance.  It is a small duck holding a knife with his little duck wing, and it means business.")

    duck_health = 150
    while duck_health > 0 and character["health_points"] > 0:
        print(f"The duck's health: {duck_health}")
        print(f"{character['name']}'s HP: {character['health_points']} | Power: {character['power']}")
        print("What will you do?")
        print("1. Use ability")
        print("2. Use potion")

        action = input("Enter 1 or 2: ")
        print()

        if action == "1":
            damage = use_ability(character)
        elif action == "2":
            use_potion(character)
            damage = 0
        else:
            print("Invalid choice. Turn wasted.")
            damage = 0

        duck_health -= damage

        if duck_health <= 0:

            #ending flavor text
            print("Several days have passed, feeling like months, perhaps years, as Frank battled the duck, not just for his own life, but for the right to visit a children's theme park using money plundered from helpless animals.")
            print("With one final blow, the duck was struck down, and Frank stood over its tiny, ruined corpse in hard-won victory.")
            print("These last few days were full of blood, sweat, and tears, though most of the tears came from the slain wildlife.  But he had done it.")
            print("Frank would not be deterred from his fund-raising expedition, regardless of the distressed onlookers questioning his sanity as they watched in complete disbelief.")
            print("'Does anyone know who this crazy guy is' and 'Holy **** that guy just punched a duck in the face' were common utterances, though Frank was unbothered.")
            print("Children who witnessed this violence would never be the same, and neither would their parents.  The police were called multiple times, always arriving too late, always to no avail.")
            print("Frank would not be denied his vacation to Tatertown, no matter how many videos surfaced on Youtube of him beating down squirrels that, for some reason, contained gold pieces.")
            print("Punch after punch, fireball after fireball, until finally:  the goal was met.")
            print("Victorious, Frank got on the next boat destined for Tatertown and lived happily ever after until he returned home the next day and was jailed for animal cruelty.")
      
            return

        # duck counterattacks
        duck_damage = random.randint(12, 20)
        character["health_points"] -= duck_damage
        print(f"The duck attacks with a little duck-sized knife! {character['name']} loses {duck_damage} HP.")
        print(f"{character['name']}'s health is now {character['health_points']}\n")

        #gameover feedback specific to the duck
        if character["health_points"] <= 0:
            print(f"{character['name']} was defeated by the tiny duck...")
            print("Clutching the 200 gold pieces within his hand, he watches as the boat to Tatertown sails off without him. The boat to the afterlife, however, patiently awaits...")
            return              

#Call the main
if __name__ == "__main__":
    main()
