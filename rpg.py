import random

class Lion:
    def __init__(self, name, health, strength, defense):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense

class Monster:
    def __init__(self, name, health, strength, defense):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense

def battle(lion, monster):
    print(f"A {monster.name} appears!")
    while lion.health > 0 and monster.health > 0:
        lion_attack = random.randint(1, lion.strength)
        monster_attack = random.randint(1, monster.strength)
        lion_defense = random.randint(1, lion.defense)
        monster_defense = random.randint(1, monster.defense)

        lion_damage = max(0, lion_attack - monster_defense)
        monster_damage = max(0, monster_attack - lion_defense)

        lion.health -= monster_damage
        monster.health -= lion_damage

        print(f"{lion.name} attacks {monster.name} for {lion_damage} damage!")
        print(f"{monster.name} attacks {lion.name} for {monster_damage} damage!")
        print(f"{lion.name} has {lion.health} health remaining!")
        print(f"{monster.name} has {monster.health} health remaining!")

    if lion.health > 0:
        print(f"{lion.name} defeats {monster.name}!")
    else:
        print(f"{lion.name} has been defeated by {monster.name}.")

# Create the player and monster
lion = Lion("Simba", 100, 10, 5)
monster = Monster("Goblin", 50, 5, 2)

# Start the battle
battle(lion, monster)
