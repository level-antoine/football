import math
import random
import numpy as np

from matplotlib import pyplot as plt
from absl import flags

from gfootball.env import config
from gfootball.env import football_env
from gfootball.env import football_action_set

FLAGS = flags.FLAGS
flags.DEFINE_bool('real_time', True,
                  'If true, environment will slow down so humans can play.')


class Environment:

    _length = [-1, 1]
    _width = [-0.42, 0.42]

    cfg_values = {
        'action_set': 'simple',
        'custom_display_stats': 'simple115',
        'dump_full_episodes': True,
        'real_time': True,
        'level': '5_vs_5',
        'render': True,
    }

    _left_goal_dimension = [
        -1, [i for i in np.arange(-0.044, 0.045, 0.001)]
    ]

    _right_goal_dimension = [
        -1, [i for i in np.arange(-0.044, 0.045, 0.001)]
    ]

    def __init__(self, env_name, actions):
        cfg = config.Config(self.cfg_values)
        self.env = football_env.FootballEnv(cfg)
        if cfg['render']:
            self.env.render()
        obs = self.env.reset()
        while True:
            obs, reward, done, info = self.env.step(self.env.action_space.sample())
            self._left_team_coo = obs[0]['left_team']
            self._right_team_coo = obs[0]['right_team']
            self._ball_owned_team = obs[0]['ball_owned_team']
            #if self._ball_owned_team == 0:
            #    self._actif_player_coo = self._left_team_coo[obs[0]['ball_owned_player']]
            #else:
            #    self._actif_player_coo = None
            print('------------------------------------------------------')
            print(obs[0]['ball_owned_player'])
            for i in self._left_team_coo:
                print(i)
            #print(self.in_front_of_the_goal())
            #print(self.distance_between_the_active_player_and_the_goal())

    def in_front_of_the_goal(self):
        if self._actif_player_coo is None: return 0
        for i in self._left_goal_dimension[1]:
            print(i)
            if self._actif_player_coo[1] == i:
                return 1
        return 0

    def distance_between_the_active_player_and_the_goal(self):
        if self._actif_player_coo is None: return None
        AB = math.sqrt(math.pow(self._actif_player_coo[1], 2))
        BC = math.sqrt(math.pow(self._length[1], 2))
        AC = math.pow(AB, 2) + math.pow(BC, 2)
        return math.sqrt(AC)

    def opponent_between_the_goal_and_the_active_player(self):
        number = 0
        if self._actif_player_coo is None: return None
        for opponent in self._right_team_coo:
            if self._actif_player_coo[0] < opponent[0]:
                number += 1
        return number


if __name__ == '__main__':
    env = Environment('11_vs_11_stochastic', 'simple')
