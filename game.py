import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()

    def create_buttons(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text='', font='normal 20 bold', width=5, height=2,
                                   command=lambda row=row, col=col: self.on_button_click(row, col))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def on_button_click(self, row, col):
        if self.buttons[row][col]['text'] == '' and not self.is_winner():
            self.buttons[row][col]['text'] = self.current_player
            self.board[row][col] = self.current_player
            if self.is_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("Tic Tac Toe", "The game is a tie!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def is_winner(self):
        return (self.check_rows() or self.check_columns() or self.check_diagonals())

    def check_rows(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != '':
                return True
        return False

    def check_columns(self):
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                return True
        return False

    def check_diagonals(self):
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] != '') or \
           (self.board[0][2] == self.board[1][1] == self.board[2][0] != ''):
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == '':
                    return False
        return True

    def reset_board(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]['text'] = ''

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

