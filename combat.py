# combat.py
# This file contains the battle function.

def fight(player, enemy):
    """Let the player and enemy take turns attacking."""
    print("\\nA battle begins against", enemy["name"] + "!")

    while player["hp"] > 0 and enemy["hp"] > 0:
        print("\\nYour HP:", player["hp"], "|", enemy["name"], "HP:", enemy["hp"])
        action = input("Press A to attack or P to use a potion: ").lower()

        if action == "p":
            if "Small Potion" in player["inventory"]:
                player["inventory"].remove("Small Potion")
                player["hp"] = min(player["max_hp"], player["hp"] + 12)
                print("You used a potion and recovered health.")
            else:
                print("You do not have a Small Potion.")
                continue
        elif action == "a":
            damage = player["attack"]
            enemy["hp"] -= damage
            print("You deal", damage, "damage!")
        else:
            print("Choose A to attack or P to use a potion.")
            continue

        if enemy["hp"] > 0:
            player["hp"] -= enemy["attack"]
            print(enemy["name"], "hits you for", enemy["attack"], "damage!")

    if player["hp"] > 0:
        print("You defeated", enemy["name"] + "!")
        return True

    print("\\nYou have been defeated. The forest falls into shadow...")
    return False
