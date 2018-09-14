# Computer Programming II, 6th Period
# September 10th, 2018
"""
A project the Computer Programming II PM class is working on.
"""
import tkinter as tk


class App(tk.Frame):
    def __init__(self, master):
        # Main Frame Initialization
        master.config(width=1280, height=720)
        super().__init__(master)

        # Item Dictionaries
        self.frames = {}
        self.buttons = {}
        self.labels = {}
        self.entries = {}

        self.chess_board = ChessBoard(master)
        for color in ["black", "white"]:
            print(color)
            pass  # Make the pieces needed for each team


class ChessBoard(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.board_positions = dict()
        for letter in ["A", "B", "C", "D", "E", "F", "G", "H"]:
            for number in range(8):
                if letter not in self.board_positions.keys():
                    self.board_positions.update({letter: {number + 1: tk.Frame(self)}})
                else:
                    self.board_positions[letter].update({number + 1: tk.Frame(self)})

    def __str__(self):
        pass


class ChessPiece:
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color

    def __str__(self):
        pass


class King(ChessPiece):
    def __init__(self, pos, color):
        super().__init__(pos, color)

    def __str__(self):
        pass


class Queen(ChessPiece):
    def __init__(self, pos, color):
        super().__init__(pos, color)

    def __str__(self):
        pass


class Rook(ChessPiece):
    def __init__(self, pos, color):
        super().__init__(pos, color)

    def __str__(self):
        pass


class Bishop(ChessPiece):
    def __init__(self, pos, color):
        super().__init__(pos, color)

    def __str__(self):
        pass


class Knight(ChessPiece):
    def __init__(self, pos, color):
        super().__init__(pos, color)

    def __str__(self):
        pass


class Pawn(ChessPiece):
    def __init__(self, pos, color):
        super().__init__(pos, color)

    def __str__(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    main_frame = App(root)
    root.mainloop()
