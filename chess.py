import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import os


class Board:
    def __init__(self) -> None:
        self.board = []

        for i in range(8):
            self.board.append([(x + i + 1) % 2 for x in range(8)])

    def plot_board(self, move=None) -> None:

        plt.matshow(self.board, cmap=ListedColormap(["k", "w"]))
        ax = plt.gca()
        ax.set_xticks([x - 0.5 for x in range(1, 9)], minor=True)
        ax.set_yticks([y - 0.5 for y in range(1, 9)], minor=True)
        ax.set_xticklabels([0, "A", "B", "C", "D", "E", "F", "G", "H"])
        ax.set_yticklabels([0, 8, 7, 6, 5, 4, 3, 2, 1])
        plt.grid(which="minor", ls="-", lw=2)
        plt.grid(c="k", lw="0", which="minor")

        if not os.path.exists("static/images"):
            os.mkdir("static/images")

        plt.savefig("static/images/board.png", bbox_inches="tight")


def convert_coords(coord) -> tuple:
    coord = coord.strip()

    letters = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}

    x = letters[coord[0].upper()]
    y = 8 - int(coord[1])

    return (x, y)


def check_move(colour, piece, start, end) -> bool:

    if start == end:
        return "No move made"

    if start == end:
        return "No move made"

    start = convert_coords(start)
    end = convert_coords(end)

    if piece == "Rook":
        if start[0] == end[0] or start[1] == end[1]:
            return True

    return False
