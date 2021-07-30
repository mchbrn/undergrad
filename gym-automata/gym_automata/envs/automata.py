from automaton import Automaton
from host import Host
import numpy as np
import pandas as pd
from random import random
from random import seed
import random
import networkx as nx

class Automata:
    def __init__(self, automata_number_of, hosts_number_of):
        self.automata_number_of = automata_number_of
        self.hosts_number_of = hosts_number_of
        self.automata = np.zeros((automata_number_of + 2), dtype=object)
        self.locations = np.zeros((hosts_number_of, 3), dtype='uint16')
        self.report_initial = []
        self.isolation_tank = np.zeros((hosts_number_of, 1), dtype=object)

        graph = nx.Graph()

        # declare all graph edges between vertices
        graph_edges = [(0,3), (0,4), (0,5), (0,6), (0,7),
                       (1,3), (1,6),
                       (2,5), (2,8),
                       (3,6), (3,9),
                       (4,7),
                       (5,8),
                       (6,9)]

        graph.add_edges_from(graph_edges)

        # load environment data
        df_env = pd.read_csv('../../../data/environment.csv')

        # instantiate automaton objects
        for index, data in df_env.iterrows():
            number = int(data['number'])
            name = data['name']
            x = int(data['x'])
            y = int(data['y'])
            population = int(data['population'])
            edges = list(graph.adj[number])
            update = "\rBuilding automata: " + str(number)
            print(update, end="")
            self.automata[number] = Automaton(number, name, x, y, population, edges)

        print("\n")

        # load population data
        df_pop = pd.read_csv('../../../data/population2.csv')

        initial_susceptible = []
        initial_asymptomatic = []

        # instantiate host objects
        for index, data in df_pop.iterrows():
            number = int(data['number'])
            age = data['age']
            sex = data['sex']
            ethnicity = data['ethnicity']
            health = data['health']
            state = int(data['state'])
            town = int(data['town'])
            host = Host(number, age, sex, ethnicity, health, state, town)
            # add host to automaton
            location = self.automata[town].setHost(host)
            # index host cell and automaton in array
            self.locations[number][0] = location[0]
            self.locations[number][1] = location[1]
            self.locations[number][2] = town
            if state == 0:
                attributes = [age, sex, ethnicity, health, town]
                initial_susceptible.append(attributes)
            elif state == 2:
                attributes = [age, sex, ethnicity, health, town]
                initial_asymptomatic.append(attributes)
            update = "\rBuilding hosts: " + str(number)
            print(update, end="")

        self.report_initial.append(initial_susceptible)
        self.report_initial.append(initial_asymptomatic)

    # move host to new automaton
    def changeAutomaton(self, host, automaton_number):
        x, y = self.automata[automaton_number].setHost(host)

        cell = [x, y]
        cells_available, cells_empty = self.automata[automaton_number].getNeighbourhood(cell)
        print("cells available")
        for cell_a in cells_available:
            print(cell_a)
            x_a, y_a = cell_a
            print(self.automata[automaton_number].coordinates[x_a][y_a])

        print("taken cells")
        for cell_e in cells_empty:
            print(cell_e)
            x_e, y_e = cell_e
            print(self.automata[automaton_number].coordinates[x_e][y_e])

        return [x, y]

    def getPositions(self, host_number):
        x = self.locations[host_number][0]
        y = self.locations[host_number][1]
        automaton_number = self.locations[host_number][2]
        return [x, y, automaton_number]

    def setPositions(self, host_number, x, y, automaton_number):
        self.locations[host_number][0] = x
        self.locations[host_number][1] = y
        self.locations[host_number][2] = automaton_number

    def startIsolation(self, host, host_number):
        host.self_isolating = True
        print("starting self-isolation")
        print(host)
        x, y, automaton = self.getPositions(host_number)
        self.automata[automaton].removeHost(x, y)
        self.isolation_tank[host_number][0] = host
        self.setPositions(host_number, 10, 0, 0)

    def endIsolation(self, host_number):
        host = self.isolation_tank[host_number][0]
        print("end self-isolation")
        print(host)
        host.self_isolating = False
        x, y = self.automata[host.home].setHost(host)
        self.isolation_tank[host_number] = 0
        self.setPositions(host_number, x, y, host.home)

    def terminateHost(self, host_number, self_isolating):
        if self_isolating:
            self.isolation_tank[host_number] = 0
        else:
            x, y, automaton = self.getPositions(host_number)
            self.automata[automaton].removeHost(x, y)

        self.setPositions(host_number, 12, 0, 0)
