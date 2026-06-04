import math
import tkinter as tk
from tkinter import messagebox


class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Tic-Tac-Toe (Minimax)")
        
        self.ai = 'O'
        self.human = 'X'
        self.board = [' ' for _ in range(9)]
        
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        # Game grid configuration
        for i in range(9):
            # The lambda captures the current value of i as idx
            btn = tk.Button(
                self.root, text=' ', font=('Arial', 24, 'bold'), 
                width=5, height=2, bg='#f0f0f0',
                command=lambda idx=i: self.human_move(idx)
            )
            # FIXED: Changed 'idx' to 'i' to match the loop iterator variable
            row = i // 3
            col = i % 3
            btn.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(btn)
            
        # Reset Button
        reset_btn = tk.Button(
            self.root, text="Reset Game", font=('Arial', 12),
            command=self.reset_game, bg='#d9e2ec'
        )
        reset_btn.grid(row=3, column=0, columnspan=3, sticky="s", pady=10)

    def human_move(self, index):
        if self.board[index] == ' ' and not self.check_winner(self.ai) and not self.check_winner(self.human):
            self.board[index] = self.human
            self.buttons[index].config(text=self.human, state='disabled', disabledforeground='#1976D2')
            
            if self.evaluate_game_over():
                return
                
            # Trigger AI Turn immediately after a tiny delay
            self.root.after(300, self.ai_move)

    def ai_move(self):
        best_move = self.find_best_move()
        if best_move is not None:
            self.board[best_move] = self.ai
            self.buttons[best_move].config(text=self.ai, state='disabled', disabledforeground='#D32F2F')
            self.evaluate_game_over()

    def find_best_move(self):
        best_score = -math.inf
        best_move = None
        for move in self.get_available_moves():
            self.board[move] = self.ai
            score = self.minimax(-math.inf, math.inf, False)
            self.board[move] = ' '
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def minimax(self, alpha, beta, is_maximizing):
        if self.check_winner(self.ai): return 10
        if self.check_winner(self.human): return -10
        if ' ' not in self.board: return 0

        if is_maximizing:
            max_eval = -math.inf
            for move in self.get_available_moves():
                self.board[move] = self.ai
                evaluation = self.minimax(alpha, beta, False)
                self.board[move] = ' '
                max_eval = max(max_eval, evaluation)
                alpha = max(alpha, evaluation)
                if beta <= alpha: break
            return max_eval
        else:
            min_eval = math.inf
            for move in self.get_available_moves():
                self.board[move] = self.human
                evaluation = self.minimax(alpha, beta, True)
                self.board[move] = ' '
                min_eval = min(min_eval, evaluation)
                beta = min(beta, evaluation)
                if beta <= alpha: break
            return min_eval

    def get_available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def check_winner(self, player):
        win_conditions = [
            [0,1,2], [3,4,5], [6,7,8], [0,3,6], 
            [1,4,7], [2,5,8], [0,4,8], [2,4,6]
        ]
        return any(all(self.board[pos] == player for pos in cond) for cond in win_conditions)

    def evaluate_game_over(self):
        if self.check_winner(self.human):
            messagebox.showinfo("Game Over", "Unbelievable! You won.")
            return True
        elif self.check_winner(self.ai):
            messagebox.showinfo("Game Over", "AI wins! Minimax is flawless.")
            return True
        elif ' ' not in self.board:
            messagebox.showinfo("Game Over", "It's a draw!")
            return True
        return False

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        for btn in self.buttons:
            btn.config(text=' ', state='normal', bg='#f0f0f0')


if __name__ == "__main__":
    main_window = tk.Tk()
    app = TicTacToeGUI(main_window)
    main_window.mainloop()