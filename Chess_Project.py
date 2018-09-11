# Computer Programming II, 6th Period
# September 10th, 2018
"""
A project the Computer Programming II PM class is working on.
"""
import tkinter as tk


class App(tk.Frame):
    def __init__(self, master):
        # Main Frame Initialization
        super().__init__(master)

        # Item Dictionaries
        self.frames = {}
        self.buttons = {}
        self.labels = {}
        self.entries = {}


class ChessBoard:
    def __init__(self):
        pass

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
