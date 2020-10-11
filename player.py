import matplotlib.pyplot as plt
import random

class Player(object):

    """Docstring for Player. """

    def moveLeft(self, arg):
        print("moveLeft is called")
        self._x = self._x + 1.0
        return 'Left, {0}!'.format(arg)

    def moveRight(self, arg):
        self._x = self._x - 1.0
        return 'Right, {0}!'.format(arg)

    def moveDown(self, arg):
        self._y = self._y - 1.0
        return 'Down, {0}!'.format(arg)

    def moveUp(self, arg):
        self._y = self._y + 1.0
        return 'Up, {0}!'.format(arg)

    def __init__(self, name, color="red"):
        self._name = name
        self._x = 4
        self._color = color
        if (name == "One"):
            self._y = 0
        else:
            self._y = 8
        self._actions = {0 : self.moveLeft, 1 : self.moveRight, 2 : self.moveDown,3 : self.moveUp}
        self._actionsList = [self.moveLeft,self.moveRight,self.moveDown,self.moveUp]
        print(self._actionsList)

    def getCircle(self):
        return plt.Circle((self._x, self._y), 0.5, color=self._color, fill=True)


    def play(self):
        selAction = random.randint(0, 3)
        arg = []
        self._actions[selAction](arg)
        #print(self._actionsList[0])
        #motion = random.choice(list(self._actions.values()))
        #motion()
