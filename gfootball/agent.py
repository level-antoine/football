import numpy as np
from gfootball.env import config
from gfootball.env import football_env
from gfootball.environment import Environment
from gfootball.state import State


class Agent:

    def __init__(self, g, env):
        self.g = g
        self.env = env
        self.matrix = np.array([self.env.get_actions()])
        self.matrix = np.insert(self.matrix[0], 0, '*', axis=0)
        self.width = len(self.env.get_actions())
        self.length = 0


    def add_state(self, state):
        # Array to be added as row
        row_to_be_added = np.zeros(len(self.env.get_actions()), dtype=object)
        print(row_to_be_added)
        row_to_be_added = np.insert(row_to_be_added, 0, state, axis=0)
        # Adding row to numpy array
        self.matrix = np.vstack((self.matrix, row_to_be_added))
        self.length += 1


    def state_exist(self, state):
        for i in range(1, len(self.matrix)):
            if self.matrix[i, 0].equals:
                return i
        return False


    def print_agent_position(self):
        for i in range(0, self.env.length):
            for j in range(0, self.env.width):
                if self.env.matrix[i, j].active_player:
                    return [i, j]



    def run_episode(self):
        #print(self.env.matrix[self.print_agent_position()[0], self.print_agent_position()[1]].toString())
        self.add_state(State())
        if self.state_exist(self.env.matrix[self.print_agent_position()[0], self.print_agent_position()[1]]) is not False:
            #chercher le meilleur coup
            pass
        else:
            #créer un nouveau state
            pass

def random_step(self, state, nb_steps_max):
    pass


def update_matrix(self, state, action):
    pass


def run_episode(self, state, n):
    pass


def run(self, state):
    pass


def greedy(self, state):
    """
    self.egreedy_time = time.time()
    self.map = self.env.matrix
    i = 0
    gain = (None, None, -np.inf)
    while i < 20 and gain[2] != 10:
        self.egreedy_steps += 1
        gain = (None, None, -np.inf)
        e = np.random.random()
        self.env.matrix[state[1], state[0]] = 0
        if e < 0.9:
            for action in self.env.get_possible_actions(state):
                state = self.env.step(state, action)
                if action == 'N':
                    if gain[2] < self.env.matrix[state[1], state[0]]:
                        gain = ('N', [state[0], state[1]], self.env.matrix[state[1], state[0]])
                if action == 'E':
                    if gain[2] < self.env.matrix[state[1], state[0]]:
                        gain = ('E', [state[0], state[1]], self.env.matrix[state[1], state[0]])
                if action == 'S':
                    if gain[2] < self.env.matrix[state[1], state[0]]:
                        gain = ('S', [state[0], state[1]], self.env.matrix[state[1], state[0]])
                if action == 'W':
                    if gain[2] < self.env.matrix[state[1], state[0]]:
                        gain = ('W', [state[0], state[1]], self.env.matrix[state[1], state[0]])
            state = gain[1]
        else:
            action = np.random.choice(self.env.get_possible_actions(state))
            state = self.env.step(state, action)
            gain = (action, state, self.env.matrix[state[1], state[0]])
        i += 1
        self.env.matrix[state[1], state[0]] = 1
    if gain[2] == 10:
        print("Le pirate a trouvé le trésor")
    else:
        print("Le pirate n'a pas trouvé le trésor")
    self.egreedy_time = time.time() - self.egreedy_time
"""


def qlearning(self, state):
    """
    self.qlearning_time = time.time()
    self.run_episode(self.init_state, 10000)
    gain = -np.inf
    while gain != 10:
        self.qlearning_steps += 1
        position = state[1] * (self.env.matrix.shape[1]) + state[0]
        max = -np.inf
        ind = 0
        e = np.random.random()
        if e < 0.9:
            for i in range(0, self.matrix.shape[1]):
                if self.matrix[position, i] > max:
                    max = self.matrix[position, i]
                    ind = i
            if ind == 0:
                next_state = self.env.step(state, 'N')
            if ind == 1:
                next_state = self.env.step(state, 'S')
            if ind == 2:
                next_state = self.env.step(state, 'E')
            if ind == 3:
                next_state = self.env.step(state, 'W')
        else:
            actions = self.env.get_possible_actions(state)
            next_state = self.env.step(state, np.random.choice(actions))
        gain = self.env.matrix[next_state[1], next_state[0]]
        state = next_state
    self.qlearning_time = time.time() - self.qlearning_time
    """


if __name__ == '__main__':
    environment = Environment(3, 3, '5_vs_5', 'simple')
    agent = Agent(0.9, environment)
    agent.run_episode()
