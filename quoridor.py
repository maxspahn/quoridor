import matplotlib.pyplot as plt
import matplotlib.text as text
import matplotlib.patches as patches
import numpy as np
from player import Player
import time


class Quoridor(object):

    """Docstring for Quoridor. """

    def __init__(self):
        self.player1 = Player("One", color="blue")
        #self.player2 = Player("Two", color="red")
        self.initPlot()
        print("Initialized Game")

    def initPlot(self):
        # Make a 9x9 grid
        self.image = np.zeros(shape=(9, 9))
        for i in range(9):
            for j in range(9):
                self.image[i][j] = (i + j) % 2
        self.row_labels = range(1, 10)
        self.col_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        plt.ion()
        plt.show()
        plt.matshow(self.image)
        self._ax = plt.gca()
        print(self.row_labels)
        plt.xticks(range(9), self.col_labels)
        plt.yticks(range(9), self.row_labels)
        self._ax.add_artist(self.player1.getCircle())
        #self._ax.add_artist(self.player2.getCircle())

    def plot(self):
        for circle in self._ax.findobj(patches.Circle):
            circle.remove()
        self._ax.add_artist(self.player1.getCircle())
        #self._ax.add_artist(self.player2.getCircle())
        plt.draw()
        plt.pause(0.01)

    def play(self):
        for i in range(100):
            self.player1.play()
            #self.player2.play()
            input("Press [enter] to continue")
            self.plot()
        print("Finished Game")

    def run(self):
        self.player1.train(500000)

    def printHello(self):
        print("Hello")


if __name__ == "__main__":
    myGame = Quoridor()
    myGame.run()
