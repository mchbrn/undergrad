import gym
from gym import error, spaces, utils
from gym.utils import seeding

class Automata(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        pass
    
    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self, mode='human'):
        pass

    def close(self):
        pass

class Automaton:
    def __init__(self, number, name, x, y, edges, hosts):
        self.number = number
        self.name = name
        self.x = x
        self.y = y
        self.edges = edges
        self.hosts = hosts

    def lock():
        pass
    
    def unlock():
        pass

class Host:
    def __init__(self, age, sex, ethnicity, health, activity, state, vertex, cell):
        self.age = age
        self.sex = sex
        self.ethnicity = ethnicity
        self.health = health
        self.activity = activity
        self.state = state
        self.vertex = vertex
        self.cell = cell

    def move():
        pass

    def changeState():
        pass

    def infect():
        pass


