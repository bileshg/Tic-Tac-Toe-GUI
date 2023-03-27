import tkinter as tk
import tkinter.font as font


class TicTacToe(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.board = None
        self.turn = None

        self.message_label = None
        self.button_grid = None
        self.reset_button = None

        self.pack()
        self.create_widgets()
        self.new_game()

    def create_widgets(self):
        self.message_label = tk.Label(self, text='Tic Tac Toe')
        self.message_label.grid(row=0, column=0, columnspan=3, pady=10)

        button_font = font.Font(weight='bold')
        self.button_grid = []
        for i in range(3):
            button_row = []
            for j in range(3):
                button = tk.Button(self,
                                   text=' ',
                                   width=10,
                                   height=5,
                                   font=button_font,
                                   command=lambda r=i, c=j: self.play(r, c))
                button.grid(row=i + 1, column=j, padx=5, pady=5)
                button_row.append(button)
            self.button_grid.append(button_row)

        self.reset_button = tk.Button(self,
                                      text='Reset',
                                      command=self.new_game)
        self.reset_button.grid(row=4, column=0, columnspan=3, pady=10)

    def new_game(self):
        self.board = [[f'{i * 3 + j + 1}' for j in range(3)] for i in range(3)]
        self.turn = 0
        self.message_label.configure(text="New Game! X's Turn")
        for row in self.button_grid:
            for button in row:
                button.configure(text=' ', state='active')

    def play(self, row, col):
        button = self.button_grid[row][col]
        if button['state'] == 'active':
            current_player = 'X' if self.turn % 2 == 0 else 'O'
            color = 'blue' if self.turn % 2 == 0 else 'red'
            button.configure(text=current_player,
                             disabledforeground=color,
                             state='disabled')
            self.board[row][col] = current_player
            self.turn += 1

            winner = self.get_winner()
            if winner is not None:
                self.end_game(winner)
            elif self.turn == 9:
                self.end_game('Tie')
            else:
                current_player = 'X' if self.turn % 2 == 0 else 'O'
                self.message_label.configure(text=f"{current_player}'s turn")

    def get_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
            elif self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[0][i]

        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]

        elif self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]

        else:
            return None

    def end_game(self, winner):
        self.message_label.configure(
            text=f"{winner} wins!" if winner != 'Tie' else 'Tied!')
        for row in self.button_grid:
            for button in row:
                button.configure(state='disabled')


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Tic Tac Toe')
    game = TicTacToe(root)
    game.mainloop()
