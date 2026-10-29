# characters.py
# This file stores the player, NPC, monsters, boss, and items.

player = {
    "name": "Adventurer",
    "hp": 30,
    "max_hp": 30,
    "attack": 6,
    "inventory": []
}

wizard = {
    "name": "Elder Rowan",
    "message": "The Shadow Dragon stole the Heart Crystal!"
}

# Five regular monsters. Each one has a name, health, and attack power.
monsters = [
    {"name": "Moss Goblin", "hp": 10, "attack": 3, "position": (1, 5), "symbol": "M"},
    {"name": "Cave Bat", "hp": 8, "attack": 2, "position": (2, 10), "symbol": "M"},
    {"name": "Bog Slime", "hp": 12, "attack": 3, "position": (4, 7), "symbol": "M"},
    {"name": "Skeleton Scout", "hp": 14, "attack": 4, "position": (5, 3), "symbol": "M"},
    {"name": "Cursed Wolf", "hp": 16, "attack": 4, "position": (6, 11), "symbol": "M"}
]

boss = {
    "name": "The Shadow Dragon",
    "hp": 28,
    "attack": 5,
    "position": (6, 7)
}

# Seven items, including the three crystal fragments needed for the quest.
items = [
    {"name": "Small Potion", "position": (1, 2), "kind": "potion"},
    {"name": "Iron Sword", "position": (2, 4), "kind": "sword"},
    {"name": "Crystal Fragment 1", "position": (1, 9), "kind": "fragment"},
    {"name": "Wooden Shield", "position": (3, 11), "kind": "shield"},
    {"name": "Crystal Fragment 2", "position": (4, 3), "kind": "fragment"},
    {"name": "Crystal Fragment 3", "position": (5, 9), "kind": "fragment"},
    {"name": "Healing Herb", "position": (6, 2), "kind": "herb"}
]
