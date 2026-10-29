# main.py
# Shadowfall: The Lost Crystal
# Move with W (up), S (down), A (left), D (right). Q quits.

from world import ROWS, COLS, draw_map
from characters import player, wizard, monsters, boss, items
from combat import fight

quest_accepted = False
quest_complete = False
boss_defeated = False
wizard_position = (1, 1)
game_running = True


def show_status():
    """Display the player's health and inventory."""
    print("\n=== PLAYER STATUS ===")
    print("Health:", player["hp"], "/", player["max_hp"])
    print("Attack:", player["attack"])
    if player["inventory"]:
        print("Inventory:", ", ".join(player["inventory"]))
    else:
        print("Inventory: empty")


def get_places():
    """Build a dictionary of map symbols for things still on the map."""
    places = {}

    if not quest_complete:
        places[wizard_position] = "N"

    for monster in monsters:
        if monster["hp"] > 0:
            places[monster["position"]] = "M"

    for item in items:
        if item["name"] not in player["inventory"]:
            places[item["position"]] = "I"

    if not boss_defeated:
        places[boss["position"]] = "B"

    return places


def talk_to_wizard():
    """Let the player accept the quest and later report back."""
    global quest_accepted, quest_complete

    if not quest_accepted:
        print("\n", wizard["name"] + " says:")
        print(wizard["message"])
        print("Find all 3 Crystal Fragments, then defeat the Shadow Dragon.")
        answer = input("Accept the quest? (y/n): ").lower()
        if answer == "y":
            quest_accepted = True
            print("Quest accepted: The Lost Crystal!")
        else:
            print("The wizard will wait here.")
    elif boss_defeated and count_fragments() == 3:
        quest_complete = True
        print("\n", wizard["name"], "thanks you for saving the forest!")
        print("QUEST COMPLETE: The Lost Crystal!")
    else:
        print("\nWizard: Find the 3 Crystal Fragments and defeat the Shadow Dragon.")
        print("Fragments collected:", count_fragments(), "/ 3")
        print("Shadow Dragon defeated:", boss_defeated)


def count_fragments():
    """Count the crystal fragments currently in the player's inventory."""
    count = 0
    for item_name in player["inventory"]:
        if "Crystal Fragment" in item_name:
            count += 1
    return count


def check_current_space():
    """Handle the NPC, items, monsters, or boss at the player's position."""
    global boss_defeated

    position = (player_row, player_col)

    if position == wizard_position:
        talk_to_wizard()
        return

    for item in items:
        if item["position"] == position and item["name"] not in player["inventory"]:
            print("\nYou found:", item["name"])
            player["inventory"].append(item["name"])

            if item["kind"] == "sword":
                player["attack"] += 2
                print("The Iron Sword increases your attack by 2!")
            elif item["kind"] == "shield":
                # The shield reduces incoming damage by one point.
                for monster in monsters:
                    monster["attack"] = max(1, monster["attack"] - 1)
                boss["attack"] = max(1, boss["attack"] - 1)
                print("The shield's magic weakens enemy attacks!")
            elif item["kind"] == "herb":
                player["hp"] = min(player["max_hp"], player["hp"] + 6)
                print("The herb restores 6 health.")
            elif item["kind"] == "potion":
                print("You can use the potion during a battle by pressing P.")
            elif item["kind"] == "fragment":
                print("Crystal fragments:", count_fragments(), "/ 3")
            return

    for monster in monsters:
        if monster["position"] == position and monster["hp"] > 0:
            if not quest_accepted:
                print("\nThe monster blocks your path. Find the wizard to accept the quest!")
                return
            survived = fight(player, monster)
            if not survived:
                return
            monster["hp"] = 0
            return

    if position == boss["position"] and not boss_defeated:
        if not quest_accepted:
            print("\nThe Shadow Dragon is too powerful. Find the wizard first!")
        elif count_fragments() < 3:
            print("\nThe Shadow Dragon's shield holds! You need all 3 Crystal Fragments.")
        else:
            survived = fight(player, boss)
            if survived:
                boss_defeated = True
                print("The Shadow Dragon collapses. Return to the wizard!")
        return


print("================================")
print("   SHADOWFALL: THE LOST CRYSTAL")
print("================================")
print("Explore the forest, collect items, and save the realm.")
print("Find Elder Rowan at N to accept your quest.")
print("Controls: W = up, S = down, A = left, D = right, Q = quit")
print("Tip: Collect the Iron Sword and healing items before fighting!")

player_row = 3
player_col = 5

while game_running and player["hp"] > 0 and not quest_complete:
    draw_map(player_row, player_col, get_places())
    show_status()
    move = input("\nMove (W/A/S/D) or Q to quit: ").lower()

    if move == "w" and player_row > 1:
        player_row -= 1
    elif move == "s" and player_row < ROWS - 2:
        player_row += 1
    elif move == "a" and player_col > 1:
        player_col -= 1
    elif move == "d" and player_col < COLS - 2:
        player_col += 1
    elif move == "q":
        print("Thanks for playing Shadowfall!")
        game_running = False
    else:
        print("You cannot move there. Use W, A, S, D, or Q.")

    if game_running:
        check_current_space()

if player["hp"] <= 0:
    print("\nGAME OVER. Try again, adventurer!")
elif quest_complete:
    print("\nVICTORY! You saved the forest from the Shadow Dragon!")
