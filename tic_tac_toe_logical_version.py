# Initialize the game board and variables
board = ["-" for _ in range(9)]  # Cleaner way to create the 3x3 board
currentPlayer = "X"
winner = None
gameRunning = True

# Game board printing function
def printBoard():
    print("\n".join([
        f"{board[0]} | {board[1]} | {board[2]}",
        "---------",
        f"{board[3]} | {board[4]} | {board[5]}",
        "---------",
        f"{board[6]} | {board[7]} | {board[8]}"
    ]))
    print()  # Add extra space for readability

# Taking player input and validating it
def playerInput():
    while True:
        try:
            inp = int(input(f"Player {currentPlayer}, enter a number (1-9): ")) - 1
            if 0 <= inp < 9 and board[inp] == "-":
                board[inp] = currentPlayer
                break  # Exit the loop once valid input is provided
            else:
                print("Spot already taken or invalid input. Try again.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")

# Check for win conditions dynamically (horizontal, vertical, diagonal)
def checkWin():
    global winner, gameRunning
    winPatterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for pattern in winPatterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != "-":
            winner = board[pattern[0]]
            printBoard()
            print(f"The winner is {winner}!")
            gameRunning = False
            return  # Stop checking further if a win is found

# Check for a tie
def checkTie():
    global gameRunning
    if "-" not in board and winner is None:
        printBoard()
        print("It's a tie!")
        gameRunning = False

# Switch the player
def switchPlayer():
    global currentPlayer
    currentPlayer = "O" if currentPlayer == "X" else "X"

# Main game loop
while gameRunning:
    printBoard()
    playerInput()
    checkWin()
    if gameRunning:  # Only check for a tie if no one has won
        checkTie()
        switchPlayer()
