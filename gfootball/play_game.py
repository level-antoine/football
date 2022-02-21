# coding=utf-8
# Copyright 2019 Google LLC
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Script allowing to play the game by multiple players."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import app
from absl import flags
from absl import logging
import random
import numpy as np
import math

from gfootball.env import config
from gfootball.env import football_env
from gfootball.env import football_action_set

FLAGS = flags.FLAGS

flags.DEFINE_string('level', '', 'Level to play')
flags.DEFINE_enum('action_set', 'default', ['default', 'full'], 'Action set')
flags.DEFINE_bool('real_time', True,
                  'If true, environment will slow down so humans can play.')
flags.DEFINE_bool('render', True, 'Whether to do game rendering.')


def main(_):

  cfg_values = {
      'action_set': 'simple',
      'custom_display_stats': 'simple115',
      'dump_full_episodes': True,
      'real_time': FLAGS.real_time,
  }
  if FLAGS.level:
    cfg_values['level'] = FLAGS.level
  cfg = config.Config(cfg_values)
  env = football_env.FootballEnv(cfg)
  if FLAGS.render:
    env.render()
  obs = env.reset()

  while True:
    active_player = player_nearst_to_ball(obs)
    if check_if_adverse_player_is_nearst(active_player, obs):
      for player in obs[0]['left_team']:
        print(player)
        print(active_player)
        if player[0] != active_player[0] and player[1] != active_player[1]:
          if distance(player, active_player) < 0.2:
            obs, reward, done, info = env.step(football_action_set.action_short_pass)
          elif distance(player, active_player) < 0.5:
            obs, reward, done, info = env.step(football_action_set.action_long_pass)
        else:
          obs, reward, done, info = env.step(football_action_set.action_dribble)
    elif -0.04 < active_player[1] < 0.04:
      if np.sqrt(pow(obs[0]['ball'][1] - (-1), 2) + pow(obs[0]['ball'][1] - 0.00, 2)) < 0.3:
        obs, reward, done, info = env.step(football_action_set.action_shot)
      else:
        obs, reward, done, info = env.step(football_action_set.action_right)
    else:
      if active_player[1] > 0.00:
        obs, reward, done, info = env.step(football_action_set.action_top)
      else:
        obs, reward, done, info = env.step(football_action_set.action_bottom)
    if done:
      env.reset()


def player_nearst_to_ball(obs):
  min_dist = np.inf
  player_coo = ()
  for player in obs[0]['left_team']:
    # le plus proche du ballon
    d = distance(player, obs[0]['ball'])
    if min_dist > d:
      min_dist = d
      player_coo = (player[0], player[1])
  return player_coo


def check_if_adverse_player_is_nearst(player_pos, obs):
  for adverse_player in obs[0]['right_team']:
    if distance(player_pos, adverse_player) < 0.1:
      return True
  return False


def distance(first_obj, second_obj):
  return np.sqrt(pow(first_obj[0] - second_obj[0], 2) + pow(first_obj[1] - second_obj[1], 2))


if __name__ == '__main__':
  app.run(main)
