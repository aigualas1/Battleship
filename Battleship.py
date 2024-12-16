import random


def create_grid(x):
    """Creates a square grid for the Battleship game.

    Args:
        x (int): The size of the grid (number of rows and columns).

    Returns:
        list: A list of lists representing a grid, where each cell has the placeholder " ~~~~ ".
    """
    grid = []
    for row in range(1, x + 1, 1):
        row_list = []
        for column in range(1, x + 1, 1):
            row_list.append(" ~~~~ ")
        grid.append(row_list)
    return grid


def display_grid(x):
    """Displays a grid for the Battleship game.

    Args:
        x (list): A list of lists representing the grid to display.
    """
    for every_list in x:
        print(every_list)


def update_grid_with_ships(num_ships, specify_grid):
    """Adds 1x1 ships at random locations to a grid.

    Args:
        num_ships (int): The number of ships to add to a grid.
        specify_grid (list): A list of lists representing the grid where the ships will be placed.

    Returns:
        list: The updated grid with ships placed at random coordinates. Each ship is labeled as "Ship" followed by its number.
    """
    for ship_counter in range(1, num_ships + 1, 1):
        x_coordinate = random.randint(0, player_grid_choice - 1)
        y_coordinate = random.randint(0, player_grid_choice - 1)
        specify_grid[x_coordinate][y_coordinate] = "Ship " + str(ship_counter)
    return specify_grid


# Start the game
print("Welcome to Battleship!")

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

# Allow player to specify the grid size
player_grid_choice = int(input("How big would you like the grid to be? (Max: 26) "))

# Allow player to specify the number of ships
player_ship_choice = int(
    input(
        f"How many ships would you like there to be? (Max: {player_grid_choice * player_grid_choice}) "
    )
)

# Create grid for player
player_grid = create_grid(player_grid_choice)

# Create grid for computer
computer_grid = create_grid(player_grid_choice)

# Add ships to grid for both the player and the computer
update_grid_with_ships(player_ship_choice, player_grid)
update_grid_with_ships(player_ship_choice, computer_grid)

print()
print("Player Grid:")
display_grid(player_grid)

print()
print("Computer Grid:")
display_grid(computer_grid)

# Create variables for tracking
player_miss_counter = 0
player_hit_counter = 0

player_miss_list = []
player_hit_list = []

computer_miss_counter = 0
computer_hit_counter = 0

computer_miss_list = []
computer_hit_list = []


# Continue letting the player guess until the player hits all of the computer's ships or the computer hits all of the player's ships
while (
    player_hit_counter < player_ship_choice
    and computer_hit_counter < player_ship_choice
):
    # Ask player for a set of X/Y coordinates
    player_choice_1 = input(
        f"Which row are you targeting? ({alphabet[0]} - {alphabet[player_grid_choice - 1]}): "
    )
    player_choice_2 = int(
        input(f"Which column are you targeting? (1 - {player_grid_choice}): ")
    )
    # Validate the players input
    if (
        player_choice_1 not in alphabet[0:player_grid_choice]
        or player_choice_2 < 1
        or player_choice_2 > player_grid_choice
    ):
        print("You have provided values outside of the range. Please try again")

        continue

    # Convert the players input to valid grid coordinates:
    # player_choice_1 is converted to its corresponding index for the x-coordinate
    # Adjust player_choice_2 by subtracting 1 since the index starts at zero
    player_choice_1 = alphabet.index(player_choice_1)
    player_choice_2 = player_choice_2 - 1

    # Check computer grid and tell the player if it is a hit or miss
    if computer_grid[player_choice_1][player_choice_2] == " ~~~~ ":
        print("Miss!")
        player_miss_counter += 1
        player_miss_list.append([alphabet[player_choice_1], player_choice_2 + 1])

    # Reference: https://www.w3schools.com/python/python_strings.asp
    elif "Ship" in computer_grid[player_choice_1][player_choice_2]:
        # Inform player when a computer ship is destroyed
        print(
            f"Direct hit! The computer's {computer_grid[player_choice_1][player_choice_2]} has been destroyed!"
        )
        player_hit_counter += 1
        player_hit_list.append([alphabet[player_choice_1], player_choice_2 + 1])

    # Keep track and display the player's misses (if there are any)
    if len(player_miss_list):
        print(
            f"The player's total number of misses: {player_miss_counter}, at coordinates: {player_miss_list}"
        )

    # Keep track and display the player's hits (if there are any)
    if len(player_hit_list):
        print(
            f"The player's total number of hits: {player_hit_counter}, at coordinates: {player_hit_list}"
        )

    # Check if the player has won before the computers turn
    if player_hit_counter == player_ship_choice:
        # Reference: https://www.w3schools.com/python/ref_keyword_break.asp
        # Break out of the while loop if the player has hit all of the ships
        break

    print()

    print("Computer's turn:")

    # Computer's set of X/Y coordinates
    pc_x_coordinate = random.randint(0, player_grid_choice - 1)
    pc_y_coordinate = random.randint(0, player_grid_choice - 1)
    print(computer_miss_list)
    print(pc_x_coordinate, pc_y_coordinate)

    # Ensure the computer guesses something it hasn't guessed yet
    while [alphabet[pc_x_coordinate], pc_y_coordinate + 1] in computer_hit_list or [alphabet[pc_x_coordinate], pc_y_coordinate + 1] in computer_miss_list:
        pc_x_coordinate = random.randint(0, player_grid_choice - 1)
        pc_y_coordinate = random.randint(0, player_grid_choice - 1)
        print(computer_miss_list)
        print(pc_x_coordinate, pc_y_coordinate)

    # Check player grid and display if it is a hit or miss
    if player_grid[pc_x_coordinate][pc_y_coordinate] == " ~~~~ ":
        print("Miss!")
        computer_miss_counter += 1
        computer_miss_list.append([alphabet[pc_x_coordinate], pc_y_coordinate + 1])

    # Reference: https://www.w3schools.com/python/python_strings.asp
    elif "Ship" in player_grid[pc_x_coordinate][pc_y_coordinate]:
        # Display when a ship has been destroyed
        print(
            f"Direct hit! The player's {player_grid[pc_x_coordinate][pc_y_coordinate]} has been destroyed!"
        )
        computer_hit_counter += 1
        computer_hit_list.append([alphabet[pc_x_coordinate], pc_y_coordinate + 1])

    # Keep track and display the computer's misses (if there are any)
    if len(computer_miss_list):
        print(
            f"The computer has a total number of misses: {computer_miss_counter}, at coordinates: {computer_miss_list}"
        )

    # Keep track and display the computer's hits (if there are any)
    if len(computer_hit_list):
        print(
            f"The computer has a total number of hits: {computer_hit_counter}, at coordinates: {computer_hit_list}"
        )

# End with "Game Over" when all ships are hit for either the player or the computer
if player_hit_counter == player_ship_choice:
    print("Game Over! The player has sunk all of the computer's battleships.")
elif computer_hit_counter == player_ship_choice:
    print("Game Over! The computer has sunk all of the player's battleships.")
