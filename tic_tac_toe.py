# Import necessary modules
import tkinter as tk
from tkinter import messagebox
import random
# Define the initial state of the game board
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
# Define the game_over flag
game_over = False

# Function to update the board with a player's move
def update_board(board, row, col, player):
    board[row][col] = player
    
# Function to check if a player has won the game   
def check_win(board):
     # Check rows for a win
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != 0:
            return True
    # Check columns for a win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            return True
    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return True
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return True
    return False

# Function to get a list of empty cells on the board
def get_empty_cells(board):
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                empty_cells.append((row, col))
    return empty_cells

# Define the TicTacToeGUI class       
class TicTacToeGUI:
    # Initialize the class with the game board and buttons
    def __init__(self, master):
        self.master = master
        self.board_buttons = []
        # Create a button for each cell in the board and add it to the grid
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(master, text="", width=4, height=2, command=lambda row=row, col=col: self.button_click(row, col))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.board_buttons.append(button_row)
        # Create a restart button and add it to the grid    
        self.restart_button = tk.Button(master, text="Restart", command=self.restart)
        self.restart_button.grid(row=3, column=0, columnspan=3)
        # Disable all buttons if the game is over
        if game_over:
            for row in range(3):
                for col in range(3):
                    self.board_buttons[row][col].config(state=tk.DISABLED)

        
    # Function to handle button clicks
    def button_click(self, row, col):
        global game_over
        # Do nothing if the game is over
        if game_over:
            return
        # If the cell is empty, mark it with an "X" and update the board
        if self.board_buttons[row][col]['text'] == "":
            self.board_buttons[row][col].config(text="X")
            update_board(board, row, col, 1)
            # Check for a win by the player
            if check_win(board):
                print("Player 1 wins!")
                messagebox.showinfo("showinfo", "Player 1 wins!")
                game_over = True
                
                return
            play_ai_move(board)
            
        # Disable all buttons if the game is over
        if game_over:
            for row in range(3):
                for col in range(3):
                    self.board_buttons[row][col].config(state=tk.DISABLED)
                    
    def restart(self):
        global board, game_over
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        game_over = False
        # self.restart_button.config(state=tk.DISABLED)
        for row in range(3):
            for col in range(3):
                self.board_buttons[row][col].config(text="", state=tk.NORMAL)     
# Define a play_ai_move function that randomly selects an empty cell
def play_ai_move(board):
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                empty_cells.append((row, col))

    if empty_cells:
        row, col = random.choice(empty_cells)
        update_board(board, row, col, 2)
        game.board_buttons[row][col].config(text="O")
        if check_win(board):
            print("Player 2 wins!")
            messagebox.showinfo("showinfo", "Player 2 wins!")
            
            return
    else:
        print("Tie game!")
        messagebox.showinfo("showinfo", "Tie game!")
        
        return
# Create an instance of the Tkinter root window
root = tk.Tk()
root.geometry("200x200")
root.title('Tic Tac Toe')
game = TicTacToeGUI(root)
root.mainloop()