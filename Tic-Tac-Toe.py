import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root, ai_first=True):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.ai_first = ai_first
        self.current_player = 'O' if ai_first else 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()
        if ai_first:
            self.root.after(500, self.ai_move)

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
                if self.current_player == 'O':
                    self.root.after(500, self.ai_move)  # Delay for a better user experience

    def ai_move(self):
        best_score = float('-inf')
        best_move = None
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '':
                    self.board[row][col] = self.current_player
                    score = self.minimax(self.board, 0, False)
                    self.board[row][col] = ''
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        
        if best_move:
            row, col = best_move
            self.board[row][col] = self.current_player
            self.buttons[row][col]['text'] = self.current_player
            if self.is_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("Tic Tac Toe", "The game is a tie!")
                self.reset_board()
            else:
                self.current_player = 'X'

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner('O'):
            return 1
        if self.check_winner('X'):
            return -1
        if self.is_board_full():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == '':
                        board[row][col] = 'O'
                        score = self.minimax(board, depth + 1, False)
                        board[row][col] = ''
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == '':
                        board[row][col] = 'X'
                        score = self.minimax(board, depth + 1, True)
                        board[row][col] = ''
                        best_score = min(score, best_score)
            return best_score

    def is_winner(self):
        return (self.check_rows() or self.check_columns() or self.check_diagonals())

    def check_winner(self, player):
        return (self.check_rows(player) or self.check_columns(player) or self.check_diagonals(player))

    def check_rows(self, player=None):
        for row in self.board:
            if player:
                if row[0] == row[1] == row[2] == player:
                    return True
            else:
                if row[0] == row[1] == row[2] != '':
                    return True
        return False

    def check_columns(self, player=None):
        for col in range(3):
            if player:
                if self.board[0][col] == self.board[1][col] == self.board[2][col] == player:
                    return True
            else:
                if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                    return True
        return False

    def check_diagonals(self, player=None):
        if player:
            if (self.board[0][0] == self.board[1][1] == self.board[2][2] == player) or \
               (self.board[0][2] == self.board[1][1] == self.board[2][0] == player):
                return True
        else:
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
        self.current_player = 'O' if self.ai_first else 'X'  # Reset player to 'O' if AI starts, else 'X'
        if self.ai_first:
            self.root.after(500, self.ai_move)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root, ai_first=True)  # Set ai_first to True if AI should start
    root.mainloop()