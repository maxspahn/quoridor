import matplotlib.pyplot as plt
import random
import numpy as np
import time

import json
import sys

class Player(object):

    """Docstring for Player. """

    def __init__(self, name, color="red"):
        self._name = name
        self._x = 4
        self._color = color
        if name == "One":
            self._y = 0
        else:
            self._y = 8
        self._actions = {
            0: self.moveLeft,
            1: self.moveRight,
            2: self.moveDown,
            3: self.moveUp,
        }
        self._nbStates = 81  # 9 * 9 positions
        self._nbActions = 4
        self._qtable = dict()
        self._discount = 0.9  # 0.8 - 0.99
        self._epsilon = 0.5
        self._learning_rate = 0.1

    def moveLeft(self, arg):
        self._x = self._x + 1.0
        return "Left, {0}!".format(arg)

    def moveRight(self, arg):
        self._x = self._x - 1.0
        return "Right, {0}!".format(arg)

    def moveDown(self, arg):
        self._y = self._y - 1.0
        return "Down, {0}!".format(arg)

    def moveUp(self, arg):
        self._y = self._y + 1.0
        return "Up, {0}!".format(arg)

    def getCircle(self):
        return plt.Circle((self._x, self._y), 0.5, color=self._color, fill=True)

    def qvalue(self, state):
        if state not in self._qtable.keys():
            self._qtable[state] = 0.0
        return self._qtable[state]

    def get_open_moves(self, state):
        actions = [0, 1, 2, 3]
        x = state[0]
        y = state[1]
        states = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return states, actions

    def next_move(self):
        states, actions = self.get_open_moves(self.state())
        i = self.optimal_next(states)
        if np.random.random_sample() < self._epsilon:
            # Explore
            i = np.random.randint(0, len(states))
        return states[i], actions[i]

    def optimal_next(self, states):
        values = [self.qvalue(s) for s in states]
        return np.argmax(values)

    def state(self):
        return (self._x, self._y)

    def save_values(self, path="data/qtable.json"):
        """ Save Q values to json."""
        a = list(self._qtable)
        with open(path, "w") as out:
            for i in range(len(self._qtable)):
                out.write(str(a[i]) + ":" + str(self._qtable[a[i]]) + "\n")

    def reward(self, winner):
        if winner == self._name:
            return 50.0
        if self.gameOver(winner):
            return -100.0
        return -0.5

    def gameOver(self, winner):
        if winner:
            return True
        if self._y < 0 or self._y > 8:
            return True
        if self._x < 0 or self._x > 8:
            return True

    def update(self, reward, winner, state):
        future_val = 0
        if not winner:
            future_states, _ = self.get_open_moves(state)
            i = self.optimal_next(future_states)
            future_val = self.qvalue(future_states[i])
        # Q value update
        self._qtable[state] = ((1 - self._learning_rate) * self.qvalue(state)) + (
            self._learning_rate
            * (reward + self._learning_rate * (reward + self._discount * future_val))
        )

    def make_move(self, action):
        arg = []
        self._actions[action](arg)
        if self._name == "One":
            if self._y == 8:
                return "One"
        if self._name == "Two":
            if self._y == 0:
                return "Two"

    def step(self, verbose=False):
        """Agent make one step"""
        state, action = self.next_move()
        winner = self.make_move(action)
        reward = self.reward(winner)
        self.update(reward, winner, state)
        return (winner, reward)

    def reset(self):
        self._x = 4
        if self._name == "One":
            self._y = 0
        else:
            self._y = 8

    def train(self, episodes, history=[]):
        """Trains by playing against self.
        Each episode is a full game
        """
        x = range(episodes)
        cumulative_reward = []
        memory = []

        total_reward = 0.0
        for i in range(episodes):
            episode_reward = 0.0
            game_active = True
            # Rest of game follows strategy
            while game_active:
                winner, reward = self.step()
                episode_reward += reward
                if (self.gameOver(winner)):
                    game_active = False
                    #print(self.state())
                    #print(episode_reward)
                    self.reset()
            total_reward += episode_reward
            cumulative_reward.append(total_reward)
            #memory.append(sys.getsizeof(self.qtable) / 1024)
            # Record total reward agent gains as training progresses
            if (i % (episodes / 10) == 0) and (i >= (episodes / 10)):
                print(".")
        history.append(x)
        history.append(cumulative_reward)
        self.save_values()
        #history.append(memory)
        return history
