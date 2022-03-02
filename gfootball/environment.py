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
    
    def __init__(self, env_name, actions):
        self.env = football_env.create_environment(env_name=env_name, representation='extracted', render=True)
        self.actions = football_env.observation_preprocessing.football_action_set.action_set_dict[actions]
        self.matrix = np.zeros((self._width, self._length))
        obs = self.env.reset()
        self.generate(obs)
        
    def generate(self, observation):
        for i in range(0, self._width):
            for j in range(0, self._length):
                if observation[i, j][0] == 255:
                    print('joueur gauche : (%d;%d)' % (j, i))
                    self.matrix[i, j] = self._left_team
                if observation[i, j][1] == 255:
                    print('joueur droit : (%d;%d)' % (j, i))
                    self.matrix[i, j] = self._right_team
                if observation[i, j][3] == 255:
                    print('joueur actif : (%d;%d)' % (j, i))
                    self.matrix[i, j] += self._actif_player
                if observation[i, j][2] == 255:
                    print('ballon : (%d;%d)' % (j, i))
                    self.matrix[i, j] += self._ball


        #for i in self._goal_dimension:
        #    self.matrix[i, 0] += self._goal
        #    self.matrix[i, self._length - 1] += self._goal
    
    
    def show(self):
        plt.imshow(self.matrix, interpolation='nearest')
        plt.show()
                
        
        
if __name__ == '__main__':
    env = Environment('11_vs_11_stochastic', 'simple')
    env.show()