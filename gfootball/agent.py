import time

import gfootball.env as football_env
import random


class Agent:
    
    def __init__(self):
        pass
    
    
    
if __name__ == '__main__':
    
    env = football_env.create_environment(env_name='1_vs_1_easy', representation='extracted', render=True)

    state = env.reset()
    action_simple = football_env.observation_preprocessing.football_action_set.action_set_dict["simple"]

    obs = env.reset()

    while True:
        action = random.choice(action_simple)
        observation, reward, done, info = env.step(action)
        print('-----------------------------------------')
        i = 1
        for obs in observation:
            print(i)
            print(obs)
            i += 1
        time.sleep(1000000000)
        print(reward)
        print(done)
        print(info)
        print('-----------------------------------------')
        if done:
            env.reset()
    
    env.close()