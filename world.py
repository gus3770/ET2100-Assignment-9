# world.py
# This file controls the map and how it is displayed.

ROWS = 8
COLS = 15


def draw_map(player_row, player_col, places):
    """Print the map, the player, and any places that have not been cleared."""
    print("\n" * 3)

    for row in range(ROWS):
        for col in range(COLS):
            position = (row, col)

            if row == player_row and col == player_col:
                print("P", end=" ")
            elif row == 0 or row == ROWS - 1:
                print("#", end=" ")
            elif col == 0 or col == COLS - 1:
                print("#", end=" ")
            elif position in places:
                print(places[position], end=" ")
            else:
                print(".", end=" ")
        print()

    print("\nP = You | N = Wizard | M = Monster | I = Item | B = Boss")
