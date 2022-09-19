import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import os

class Board:
  def __init__(self) -> None:
    #  black = 0, white = 1
    self.board = []

    for i in range(8):
      self.board.append([(x+i)%2 for x in range(8)])

  def plot_board(self):

        plt.matshow(self.board, cmap=ListedColormap(["k", "w"]))
        ax = plt.gca()
        ax.set_xticks([x - 0.5 for x in range(1, 8)], minor=True)
        ax.set_yticks([y - 0.5 for y in range(1, 8)], minor=True)
        plt.grid(which="minor", ls="-", lw=2)
        plt.grid(c="k", lw="2", which="minor")

        if not os.path.exists("static/images"):
            os.mkdir("static/images")

        plt.savefig("static/images/board.png", bbox_inches="tight")