# Import Statements
import random
import time 
# Helper Functions
def print_output(decision):
    choice = "i"
    while (choice == "i"):
        choice = input("{0} [y/n] \nEnter i on your keyboard to open your inventory. ".format(decision))
        if (choice == "i"):
            print_inventory()
    if choice in ["yes", "y", "Y", "YES", "Yes", "YEs", "YeS", "Yup", "YUP", "YuP"]:
        return True
    return False
def print_inventory():
    global inventory
    for (k,v) in inventory.items():
        print("%s: %d % (k,v)")

class weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class character:
    def __init__(self, name, health, weapon = "fists"):
        self.name = name
        self.health = health
        self.weapon = weapon
    def equip_weapon(self, weapon):
        self.weapon = weapon
        print("{0} has equipped {1}.".format(self.name, weapon.name))
    def attack(self, target):
        if self.weapon:
            damage_dealt = random.randint(1, self.weapon.damage)
            target.health -= damage_dealt
            print("{0} attacks {1} with {2} for {3} damage.".format(self.name, target.name, self.weapon.name, damage_dealt))
        else:
            print("{0} has no weapon equipped and attacks with fists for {1} damage.".format(self.name, self.weapon.damage))
# Global Variable
inventory = {}
fists = weapon("Fists", 5)
torch = weapon("Torch", 10)
stick = weapon("Stick", 8)
dull_knife = weapon("Dull Knife", 6)
surfboard = weapon("Surfboard", 12)
echo_hammer = weapon("Echo Hammer", 8)
player = character("Player", 75, fists)
enemy1 = character("Small Cave Chez", 30, echo_hammer)
enemy2 = character("Top Dog Kahuna", 50, surfboard)

def battle(player, enemy):
    print(" Choose your weapon")
    print("1. Torch")
    print("2. Stick")
    print("3. Dull Knife")
    weapon_choice = input("Enter the number of your choice: ")
    if weapon_choice == "1":
        player.equip_weapon(torch)
    elif weapon_choice == "2":
        player.equip_weapon(stick)
    elif weapon_choice == "3":
        player.equip_weapon(dull_knife)
    else:
        print("Invalid choice. Defaulting to Fists.")
        player.equip_weapon(fists)

    print("\nBattle Start!")
    time.sleep(2)
    
    while player.health > 0 and enemy.health > 0:
        input("Press Enter to attack...")
        time.sleep(1)
        player.attack(enemy)
        if enemy.health <= 0:
            print("{0} has been defeated!".format(enemy.name))
            break
        enemy.attack(player)
        if player.health <= 0:
            print("{0} has been defeated!".format(player.name))
            break
        print("{0} Health: {1}, {2} Health: {3}".format(player.name, player.health, enemy.name, enemy.health))
        time.sleep(2)
    print("Battle Over!")

def game():
    global inventory
    inventory = {} 
    time.sleep(2)
    print("You find yourself at the entrance of a dark cavern.")
    time.sleep(2)
    print("Can can enter the cavern to explore or walk away.")
    while True:
        choice = input("Do you want to enter the cavern? (yes/no): ")
        if choice.lower() in ["yes", "y"]:
            print("You bravely enter the cavern.")
            time.sleep(2)
            print("As you go deeper, you see weapons. Choose one to take: Torch, Stick, Dull Knife")
            choice = input("Which weapon do you want to pick up? (torch/stick/dull knife/none): ")
            if choice.lower() == "torch":
                inventory["Torch"] = torch
                print("You picked up the Torch.")
            elif choice.lower() == "stick":
                if random.random() < 0.75:
                    print("Oh no! The stick was actually a snake.")
                    time.sleep(1)
                    return 0
                else:
                    inventory["Stick"] = stick
                    print("You picked up the Stick.")
            elif choice.lower() == "dull knife":
                inventory["Dull Knife"] = dull_knife
                print("You picked up the Dull Knife.")
            else:
                print("You decided not to pick up any weapon.")
                inventory["Fists"] = fists
                print("You will fight with your Fists.")
            time.sleep(2)
        if choice.lower() in ["no", "n"]:
            print("You decided to walk away from the cavern. Game Over.")
            return 0
        break
    print("Deeper in the cavern, there is a crossroad! Choose to go left or right.")
    while True:
        direction = input("Do you want to go left or right? (left/right): ")
        if direction.lower() == "left":
            print("You encounter a Big Kahuna Dog!")
            time.sleep(2)
            battle(player, enemy2)
            break
        elif direction.lower() == "right":
            print("You encounter a Small Cave Chez!")
            time.sleep(2)
            battle(player, enemy1)
            break
        else:
            print("Invalid choice. Please choose left or right.")
    print("Congratulations! You have completed the Cavern Adventure!")
    return 1

def main():
    alive = True
    while alive:
        result = game()
        if result == 1:
            alive = print_output("You managed to escape the cavern! Would you like to play again?")
        else:
            alive = print_output("You have died!Thank you for playing the Cavern Adventure! Would you like to try again?")

if __name__ == "__main__":
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to the Cavern Adventure!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    game() 

