import gym
from gym import error, spaces, utils
from gym.utils import seeding
import pandas as pd
from random import seed
import random
import networkx as nx

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
    """All automata begin in an unlocked state"""

    def __init__(self, number, name, x, y, edges):
        self.number = number
        self.name = name
        self.x = x
        self.y = y
        self.coordinates = []
        self.state = 1
        self.edges = edges
        
        for column in range(x):
            self.coordinates.append([])
            for row in range(y):
                self.coordinates[column].append([])

    def lock():
        pass
    
    def unlock():
        pass

    def moveHost():
        pass

class Host:
    def __init__(self, age, sex, ethnicity, employment, health, state, home, vertex):
        self.age = age
        self.sex = sex
        self.ethnicity = ethnicity
        self.employment = employment
        self.health = health
        self.state = state
        self.home = home
        self.vertex = vertex

    def initPosition(self, cell):
        self.cell = cell

    def setVertex(self, ward):
        self.vertex = ward

    def getNeighbourhoodMatrix(self, automaton):
        x, y = self.cell
        matrix = []

        # top right corner
        if (x == automaton.x - 1 and y == automaton.y - 1):
            for column in range(x - 1, x + 1, 1):
                for row in range(y - 1, y + 1, 1):
                    matrix.append([column, row])
            matrix.append([automaton.x - 2, 0])
            matrix.append([automaton.x - 1, 0])
            matrix.append([0, 0])
            matrix.append([0, automaton.y - 1])
            matrix.append([0, automaton.y - 2])
        # bottom right corner
        elif (x == automaton.x - 1 and y == 0):
            for column in range(x - 1, x + 1, 1):
                for row in range(y, y + 2, 1):
                    matrix.append([column, row])
            matrix.append([0, 1])
            matrix.append([0, 0])
            matrix.append([0, automaton.y - 1])
            matrix.append([automaton.x - 1, automaton.y - 1])
            matrix.append([automaton.x - 2, automaton.y - 1])
        # top left corner
        elif (y == automaton.y - 1 and x == 0):
            for column in range(x, x + 2, 1):
                for row in range(y - 1, y + 1, 1):
                    matrix.append([column, row])
            matrix.append([automaton.x - 1, automaton.y - 2])
            matrix.append([automaton.x - 1, automaton.y - 1])
            matrix.append([automaton.x - 1, 0])
            matrix.append([0, 0])
            matrix.append([0, 1])
        # right middle
        elif (x == automaton.x - 1 and y != automaton.y - 1):
            for column in range(x - 1, x + 1, 1):
                for row in range(y - 1, y + 2, 1):
                    matrix.append([column, row])
            matrix.append([0, y + 1])
            matrix.append([0, y])
            matrix.append([0, y - 1])
        # top middle
        elif (y == automaton.y - 1 and x != automaton.x - 1):
            for column in range(x - 1, x + 2, 1):
                for row in range(y - 1, y + 1, 1):
                    matrix.append([column, row])
            matrix.append([x - 1, 0])
            matrix.append([x, 0])
            matrix.append([x + 1, 0])
        # bottom left corner
        elif (x == 0 and y == 0):
            for column in range(x, x + 2, 1):
                for row in range(y, y + 2, 1):
                    matrix.append([column, row])
            matrix.append([1, automaton.y - 1])
            matrix.append([0, automaton.y - 1])
            matrix.append([automaton.x - 1, automaton.y - 1])
            matrix.append([automaton.x - 1, 0])
            matrix.append([automaton.x - 1, 1])
        # left middle
        elif (x == 0 and y != 0):
            for column in range(x, x + 2, 1):
                for row in range(y - 1, y + 2, 1):
                    matrix.append([column, row])
            matrix.append([automaton.x - 1, y - 1])
            matrix.append([automaton.x - 1, y])
            matrix.append([automaton.x - 1, y + 1])
        # bottom middle
        elif (y == 0 and x != 0):
            for column in range(x - 1, x + 2, 1):
                for row in range(y, y + 2, 1):
                    matrix.append([column, row])
            matrix.append([x - 1, automaton.y - 1])
            matrix.append([x, automaton.y - 1])
            matrix.append([x + 1, automaton.y - 1])
        # anywhere else
        else:
            for column in range(x - 1, x + 2, 1):
                for row in range(y - 1, y + 2, 1):
                    matrix.append([column, row])

        return matrix

    def checkNeighbourhood(self, automaton):
        matrix = self.getNeighbourhoodMatrix(automaton)
        available_cells = []

        for cell in matrix:
            x, y = cell

            # if this cells is empty or is occupied by current host
            if not automaton.coordinates[x][y] or automaton.coordinates[x][y] == self:
                available_cells.append([x, y])
        
        return available_cells

    def getNeighbours(self, automaton):
        matrix = self.getNeighbourhoodMatrix(automaton)
        neighbours = []

        for cell in matrix:
            x, y = cell

            if automaton.coordinates[x][y] or automaton.coordinates[x][y] != self:
                neighbours.append(automaton.coordinates[x][y])

        return neighbours

    def move(self, automaton):
        x, y = self.cell
        available_cells = self.checkNeighbourhood(automaton)
        choices = len(available_cells)

        if not available_cells:
            return
        else:
            seed()
            index = random.randrange(0, choices, 1)
            new_position = available_cells[index]
            new_x, new_y = new_position
            automaton.coordinates[x][y] = []
            automaton.coordinates[new_x][new_y] = self
            self.cell = new_position

    def changeState():
        pass

    def infect():
        pass

G = nx.Graph()

# define edges between vertices
elist = [(11,25), (11,17), (11,9), (25,19), (17,9), (7,25), (7,6), (6,17), 
         (6,25), (17,9), (14,7), (14,1), (1,7), (1,6), (27,6), (27,17), (27,9), 
         (27,29), (29,9), (10,14), (10,1), (10,24), (24,1), (24,6), (24,27), 
         (24,15), (3,14), (3,10), (3,13), (3,19), (13,10), (13,1), (13,24), 
         (13,18), (18,24), (18,15), (15,27), (15,29), (21,3), (21,20), (20,3), 
         (20,19), (20,12), (19,13), (19,18), (19,26), (26,18), (26,4), (4,18), 
         (4,15), (4,2), (23,21), (23,20), (23,12), (23,16), (12,19), (12,26), 
         (12,5), (5,26), (5,4), (5,28), (28,4), (28,2), (16,12), (16,5), (16,8), 
         (8,5), (8,0), (8,22), (0,5), (0,28), (22,0)]

G.add_edges_from(elist)

df_env = pd.read_csv('../../../data/environment.csv')

vertices = []

# instantiate automaton objects and add to list
for index, data in df_env.iterrows():
    vertices.append(Automaton(data['number'], data['name'], data['x'], data['y'], G.edges(index)))

df_pop = pd.read_csv('../../../data/population.csv')

hosts = []

# instantiate host objects and add to list
for index, data in df_pop.iterrows():
    hosts.append(Host(data['age'], data['sex'], data['ethnicity'], data['employment'], data['health'], data['state'], data['ward'], data['ward']))

# insert all hosts into random cells of their given automata
for host in hosts:
    my_ward = host.vertex
    x = vertices[my_ward].x
    y = vertices[my_ward].y

    while True:
        seed()
        cell_x = random.randrange(0, x, 1)
        seed()
        cell_y = random.randrange(0, y, 1)

        # check if coordinate is currently empty
        if not vertices[my_ward].coordinates[cell_x][cell_y]:
            vertices[my_ward].coordinates[cell_x][cell_y] = host
            host.initPosition([cell_x, cell_y])
            break

for x in range(1000):
    for host in hosts:
        host.move(vertices[host.vertex])
    print("time step: " + str(x))

print("done")
