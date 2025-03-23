mat = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def printBoard():
    """Function to print the Tic-Tac-Toe board."""
    for i in range(0, 9, 3):
        print(" | ".join(mat[i:i+3]))
        if i < 6:
            print("-" * 9)

def winPlayer():
    """Check if a player has won the game."""
    win_patterns = [(0,1,2), (3,4,5), (6,7,8),  # Rows
                    (0,3,6), (1,4,7), (2,5,8),  # Columns
                    (0,4,8), (2,4,6)]           # Diagonals
    for pattern in win_patterns:
        a, b, c = pattern
        if mat[a] == mat[b] == mat[c] and mat[a] in ['X', 'O']:
            print(f"Player '{mat[a]}' has won!")
            return True
    return False

def validMove():
    """Get a valid move from the player."""
    while True:
        try:
            move = int(input("Please enter 1-9 to make your move (0 to quit): "))
            if move == 0:
                print("Exiting game. Thank you for playing!")
                exit()
            if 1 <= move <= 9 and mat[move-1] not in ['X', 'O']:
                return move - 1  # Adjust for zero-based index
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")

def play_with_computer():
    """Improved computer AI."""
    # Check if computer can win
    for i in range(9):
        if mat[i] not in ['X', 'O']:
            mat[i] = 'O'
            if winPlayer():
                mat[i] = 'O'
                return i
            mat[i] = str(i + 1)  # Undo the move

    # Check if player can win and block them
    for i in range(9):
        if mat[i] not in ['X', 'O']:
            mat[i] = 'X'
            if winPlayer():
                mat[i] = 'O'
                return i
            mat[i] = str(i + 1)  # Undo the move

    # If no winning or blocking move, choose randomly
    import random
    available_moves = [i for i in range(9) if mat[i] not in ['X', 'O']]
    return random.choice(available_moves)

def start():
    """Start the game."""
    global mat  # Declare 'mat' as global at the beginning of the function
    while True:
        option = input("""Choose option:
        1. Player vs Player
        2. Player vs Computer
        Enter: """)
        if option in ['1', '2']:
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    count = 0
    printBoard()

    while count < 9:
        current_player = 'X' if count % 2 == 0 else 'O'
        print(f"Player {current_player}'s turn:")
        if option == '1' or (option == '2' and count % 2 == 0):  # Player's turn
            user_input = validMove()
        else:  # Computer's turn
            print("Computer is making a move...")
            user_input = play_with_computer()

        mat[user_input] = current_player
        printBoard()

        if winPlayer():
            break  # Stop the game if someone wins

        count += 1

    if count == 9:
        print("It's a tie!")

    replay = input("Do you want to play again? (y/n): ").lower()
    if replay == 'y':
        mat = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # Reset the board
        start()
    else:
        print("Thank you for playing! Goodbye!")

start()