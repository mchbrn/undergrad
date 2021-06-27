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

    def __init__(self, number, name, x, y, population, capacity):
        self.number = number
        self.name = name
        self.x = x
        self.y = y
        self.coordinates = []
        self.state = 1
        self.population = population
        self.capacity = capacity
        
        for column in range(x):
            self.coordinates.append([])
            for row in range(y):
                self.coordinates[column].append([])




    def setEdges(self, edges):
        self.edges = edges




    def addHost(self, host):
        while True:
            seed()
            x_coordinate = random.randrange(0, self.x, 1)
            seed()
            y_coordinate = random.randrange(0, self.y, 1)

            if not self.coordinates[x_coordinate][y_coordinate]:
                self.coordinates[x_coordinate][y_coordinate] = host
                host.initPosition([x_coordinate, y_coordinate])
                return




    def lock():
        pass



 
    def unlock():
        pass




    def notAtCapacity():
        if (self.population < self.capacity):
            return True
        else:
            return False




    def findEmptyCell():
        pass








class Host:
    def __init__(self, age, sex, ethnicity, health, state, home, vertex):
        self.age = age
        self.sex = sex
        self.ethnicity = ethnicity
        self.health = health
        self.state = state
        self.home = home
        self.vertex = vertex
        self.counter = 0




    def initPosition(self, cell):
        self.cell = cell




    def setVertex(self, vertex):
        self.vertex = vertex




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

        # don't include self in neighbourhood
        for cell in matrix:
            if cell == self:
                matrix.pop(cell)

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




    def moveCell(self, automaton, available_cells, choices):
        x, y = self.cell
        # remove host from old cell
        automaton.coordinates[x][y] = []
        seed()
        index = random.randrange(0, choices, 1)
        new_position = available_cells[index]
        new_x, new_y = new_position
        # add host to new cell
        automaton.coordinates[new_x][new_y] = self
        self.cell = new_position




    def moveVertex(self, vertices, automaton):
        available_vertices = []

        for edge in automaton.edges:
            if vertices[edge].notAtCapacity:
                available_vertices.append(edge)

        if available_vertices:
            choices = len(available_vertices)
            seed()
            index = random.randrange(0, choices, 1)
            vertex = available_vertices[index]
            x, y = self.cell
            # remove host from old automaton
            automaton.coordinates[x][y] = []
            # add host to new automaton
            vertices[vertex].addHost(self)
            self.vertex = vertices[vertex].number
            return True
        else:
            return False




    def moveHome(self, vertices, automaton):
        x, y = self.cell
        # remove host from old automaton
        automaton.coordinates[x][y] = []
        # add host to home automaton
        vertices[self.home].addHost(self)
        self.vertex = self.home




    def move(self, vertices, automaton):
        self.counter += 1
        available_cells = self.checkNeighbourhood(automaton)
        choices = len(available_cells)

        # every 1000 steps, allow host to go home
        if self.counter % 1000 == 0:
            # host is not home
            if self.vertex != self.home:
                seed()
                # 50:50 odds of returning home
                send_home = random.randrange(0, 2, 1)
                if send_home:
                    if automaton.notAtCapacity:
                        self.moveHome(vertices, automaton)
                        return True
                    else:
                        if available_cells:
                            self.moveCell(automaton, available_cells, choices)
                            return True
                        else:
                            return False
            # host is home
            else:
                if available_cells:
                    self.moveCell(automaton, available_cells, choices)
                    return True
                else:
                    return False

        # every 100 steps, allow travel to another vertex
        elif (self.counter % 100 == 0):
            seed()
            change_vertex = random.randrange(0, 2, 1)
            if change_vertex:
                if self.moveVertex(vertices, automaton):
                    return True
                else:
                    return False
            else:
                if available_cells:
                    self.moveCell(automaton, available_cells, choices)
                    return True
                else:
                    return False

        # move within current vertex
        else:
            if available_cells:
                self.moveCell(automaton, available_cells, choices)
                return True
            else:
                return False




    def changeState(host, newState):
        if newState == "I":
            host.state = newState



    def infect(self, automaton):
        neighbours = self.getNeighbours(automaton)
        for neighbour in neighbours:
            seed()
            infect = random.randint(0, 100)
            if infect > 80:
                neighbour.changeState(neighbour, "I")








# load environment data
df_env = pd.read_csv('../../../data/environment.csv')

vertices = []

# instantiate automaton objects
for index, data in df_env.iterrows():
    x = data['x']
    y = data['y']
    capacity = (x * y) / 3
    vertices.append(Automaton(data['number'], data['name'], x, y, data['population'], capacity))








# instantiate graph
graph = nx.Graph()

# define edges between vertices
edges = [(0,2), (0,5), (0,7), (0,11), (0,21),
         (1,18), (1,19),
         (2,8), (2,11), (2,24),
         (3,5), (3,9), (3,14), (3,15), (3,16),
         (4,7), (4,21),
         (5,11), (5,14),
         (6,11), (6,13), (6,23), (6,24),
         (7,21), (7,22),
         (8,13), (8,24),
         (9,14), (9,15),
         (10,19), (10,20), (10,23),
         (11,20),
         (12,17), (12,18), (12,20),
         (13,24),
         (15,16),
         (16,17), (16,20)]




graph.add_edges_from(edges)

# add edge indexes to automaton member
for index, vertex in enumerate(vertices):
    vertex.setEdges(list(graph.adj[index]))








# load population data
df_pop = pd.read_csv('../../../data/population.csv')

hosts = []

# instantiate host objects
for index, data in df_pop.iterrows():
    hosts.append(Host(data['age'], data['sex'], data['ethnicity'], data['health'], data['state'], data['town'], data['town']))

vertices[0].addHost(hosts[0])

# insert all hosts into random cells of their given automata
for host in hosts:
    vertices[host.home].addHost(host)







# start simulation
for x in range(381600):
    hosts[0].move(vertices, vertices[host.vertex])
#    for host in hosts:
#        host_moved = host.move(vertices, vertices[host.vertex])
#        if host_moved:
#            if host.state == 'I':
#                host.infect(vertices[host.vertex])
#    host_moved = hosts[0].move(vertices, vertices[host.vertex])
#    if host_moved:
#        host.infect(vertices[host.vertex])
    print("vertex: " + hosts[0].vertex)
    print("position: " + hosts[0].cell)








