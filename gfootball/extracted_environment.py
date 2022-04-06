import math

import gfootball.env as football_env
import random
import numpy as np
from matplotlib import pyplot as plt


class Environment:
    _length = 96
    _width = 72
    _left_team = 1
    _right_team = -1
    _ball = 10
    _goal = 100
    _actif_player = 2
    _goal_dimension = [34, 35, 36, 37, 38, 39, 40]
    _left_team_coo = []
    _right_team_coo = []
    _actif_player_coo = None
    _ball_coo = None

    def __init__(self, env_name, actions):
        self.env = football_env.create_environment(env_name=env_name, representation='extracted', render=True)
        self.actions = football_env.observation_preprocessing.football_action_set.action_set_dict[actions]
        obs = self.env.reset()
        while True:
            self.matrix = np.zeros((self._width, self._length))
            self.generate(obs)
            obs, reward, done, info = self.env.step(self.env.action_space.sample())
            #self.show()
            #print(self.in_front_of_the_goal())
            #print(self.distance_between_the_active_player_and_the_goal())
            #print(self.opponent_between_the_goal_and_the_active_player())
            print('------------------------------------------')
            if done:
                self.env.reset()

    def generate(self, observation):
        self._left_team_coo = []
        self._right_team_coo = []
        for i in range(0, self._width):
            for j in range(0, self._length):
                if observation[i, j][0] == 255:
                    #print('joueur gauche : (%d;%d)' % (j, i))
                    self.matrix[i, j] = self._left_team
                    self._left_team_coo.append((j, i))
                if observation[i, j][1] == 255:
                    #print('joueur droit : (%d;%d)' % (j, i))
                    self.matrix[i, j] = self._right_team
                    self._right_team_coo.append((j, i))
                if observation[i, j][3] == 255:
                    #print('joueur actif : (%d;%d)' % (j, i))
                    self.matrix[i, j] += self._actif_player
                    self._actif_player_coo = (j, i)
                if observation[i, j][2] == 255:
                    #print('ballon : (%d;%d)' % (j, i))
                    self.matrix[i, j] += self._ball
                    self._ball_coo = (j, i)
        print(self._actif_player_coo)
        print(self._ball_coo)

    def show(self):
        plt.imshow(self.matrix, interpolation='nearest')
        plt.show()
        # print(self._right_team_coo)
        # print(self._actif_player_coo)

    def in_front_of_the_goal(self):
        for i in self._goal_dimension:
            if self._actif_player_coo[1] == i:
                return 1
        return 0

    def distance_between_the_active_player_and_the_goal(self):
        AB = math.sqrt(math.pow(self._actif_player_coo[1] - self._width / 2, 2))
        BC = math.sqrt(math.pow(self._width / 2 - self._length, 2))
        AC = math.pow(AB, 2) + math.pow(BC, 2)
        return math.sqrt(AC)

    def opponent_between_the_goal_and_the_active_player(self):
        number = 0
        for opponent in self._right_team_coo:
            if self._actif_player_coo[0] < opponent[0]:
                number += 1
        return number


if __name__ == '__main__':
    env = Environment('11_vs_11_stochastic', 'simple')