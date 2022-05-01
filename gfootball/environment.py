import math
import random

import numpy
import numpy as np

from absl import flags

from gfootball.env import config, football_action_set
from gfootball.env import football_env
from gfootball.state import State

FLAGS = flags.FLAGS
flags.DEFINE_bool('real_time', True,
                  'If true, environment will slow down so humans can play.')

class Environment:
    _width = [-1, 1]
    _length = [-0.42, 0.42]
    _right_corner = [-1, 0.42]

    _left_goal_dimension = [
        -1, [i for i in np.arange(-0.044, 0.045, 0.001)]
    ]

    _right_goal_dimension = [
        -1, [i for i in np.arange(-0.044, 0.045, 0.001)]
    ]

    def __init__(self, length, width, env_name, actions):
        self.length = length
        self.width = width
        self.env_name = env_name
        self.actions = actions
        cfg = config.Config({
            'action_set': actions,
            'custom_display_stats': 'simple115',
            'dump_full_episodes': True,
            'real_time': True,
            'level': env_name,
            'render': True,
        })
        self.matrix = numpy.full((length, width), State())
        for i in range(0, length):
            for j in range(0, width):
                self.matrix[i, j] = State()
        self.env = football_env.FootballEnv(cfg)
        obs = self.env.reset()
        self.update_env(obs)

    def update_env(self, obs):
        div_length = (abs(self._length[0]) + abs(self._length[1])) / self.length
        div_width = (abs(self._width[0]) + abs(self._width[1])) / self.width
        px = self._right_corner[0]
        py = self._right_corner[1]

        for i in range(0, self.length):
            for j in range(0, self.width):
                if px + div_width * j <= obs[0]['ball'][0] <= px + div_width * (j + 1) and py - div_length * (i + 1) <= \
                        obs[0]['ball'][1] <= py - div_length * i:
                    self.matrix[i, j].ball = True
                    print("le ballon ", (i, j))
                for player in obs[0]['left_team']:
                    if px + div_width * j <= player[0] <= px + div_width * (j + 1) and py - div_length * (i + 1) <= \
                            player[1] <= py - div_length * i:
                        self.matrix[i, j].nb_left_player += 1
                count = 0
                for player in obs[0]['right_team']:
                    if px + div_width * j <= player[0] <= px + div_width * (j + 1) and py - div_length * (i + 1) <= \
                            player[1] <= py - div_length * i:
                        self.matrix[i, j].nb_right_player += 1
                        if count == 2:
                            self.matrix[i, j].active_player = True
                            print("acive player ", (i, j))
                        count += 1
                self.matrix[i, j].ball_owned_team = obs[0]['ball_owned_team']
                self.matrix[i, j].ball_owned_player = obs[0]['ball_owned_player']
                self.matrix[i, j].score_left_team = obs[0]['score'][0]
                self.matrix[i, j].score_right_team = obs[0]['score'][1]


    def step(self, action):
        obs, reward, done, info = self.env.step(action)
        self.update_env(obs)


    def get_actions(self):
        return football_action_set.action_set_dict[self.actions]


if __name__ == '__main__':
    env = Environment(3, 3,'5_vs_5', 'simple')
