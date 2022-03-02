import gfootball.env as football_env
import random

env = football_env.create_environment(env_name='1_vs_empty_goal', representation='simple115', render=False)

state = env.reset()
action_simple = football_env.observation_preprocessing.football_action_set.action_set_dict["simple"]

obs = env.reset()

print(obs[0])

while True:
  action = random.choice(action_simple)
  observation, reward, done, info = env.step(action)
  if done:
    env.reset()

env.close()