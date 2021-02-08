import gym
from gym import error, spaces, utils
from gym.utils import seeding
import pandas as pd

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
    def __init__(self, number, name, x, y):#, edges, hosts):
        self.number = number
        self.name = name
        self.x = x
        self.y = y
        #self.edges = edges
        #self.hosts = hosts

    def lock():
        pass
    
    def unlock():
        pass

class Host:
    def __init__(self, age, sex, ethnicity, employment, health, state, vertex, cell):
        self.age = age
        self.sex = sex
        self.ethnicity = ethnicity
        self.employment = employment
        self.health = health
        self.state = state
        self.vertex = vertex
        self.cell = cell

    def move():
        pass

    def changeState():
        pass

    def infect():
        pass

df_env = pd.read_csv('../../../data/environment.csv')

vertices = []

# Instantiate automaton objects and add to list
for index, data in df_env.iterrows():
    vertices.append(Automaton(data['Number'], data['Name'], data['X'], data['Y']))

print(vertices[0].name)

df_pop = pd.read_csv('../../../data/population.csv')

hosts = []

# Instantiate host objects and add to list
for index, data in df_pop.iterrows():
    hosts.append(Host(data['Age'], data['Sex'], data['Ethnicity'], data['Employment'], data['Health'], 'S', 0, 0))

print(hosts[0])
