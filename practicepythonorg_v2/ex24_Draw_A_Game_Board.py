def draw_game_board(size):
    for row in range(size):
        # Draw the horizontal lines
        print(" ---" * size)
        
        # Draw the vertical lines with empty spaces
        print("|   " * (size + 1))
    
    # Draw the final horizontal line to complete the game board
    print(" ---" * size)

# Ask the user for the size of the game board
size = int(input("Enter the size of the game board: "))

# Draw the game board
draw_game_board(size)