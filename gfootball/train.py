import gfootball.env as football_env

env = football_env.create_environment(env_name='1_vs_0_easy', representation='pixels', render=True)

state = env.reset()

while True:
  observation, reward, done, info = env.step(env.action_space.sample())
  if done:
    env.reset()

env.close()