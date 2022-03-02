import gfootball.env as football_env
import random
import numpy as np


class Environment:
    
    _length = 96
    _width = 72
    
    def __init__(self, env_name, actions):
        self.env = football_env.create_environment(env_name=env_name, representation='extracted', render=True)
        self.actions = football_env.observation_preprocessing.football_action_set.action_set_dict[actions]
        self.matrix = np.zeros((self._width, self._length))
        obs = self.env.reset()
        self.generate_map(obs)
        
    def generate_map(self, observation):
        for i in range(0, self._width - 1):
            for j in range(0, self._length - 1):
                if observation[i, j][0] == 255:
                    print('joueur gauche : (%d;%d)' % (i, j))
                    self.matrix[i, j] = 1
                if observation[i, j][1] == 255:
                    print('joueur droit : (%d;%d)' % (i, j))
                    self.matrix[i, j] = -1
                if observation[i, j][3] == 255:
                    print('joueur actif : (%d;%d)' % (i, j))
                    self.matrix[i, j] += 2
                if observation[i, j][2] == 255:
                    print('ballon : (%d;%d)' % (i, j))
                    self.matrix[i, j] += 10
                
        
        
if __name__ == '__main__':
    env = Environment('11_vs_11_stochastic', 'simple')