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
        self.automata = np.zeros((automata_number_of), dtype=object)
        self.locations = np.zeros((hosts_number_of, 3), dtype='uint16')
        self.report_initial = []
        self.isolation_tank = np.zeros((hosts_number_of, 1), dtype=object)
        self.automaton_isolation_number = automata_number_of + 1
        self.automaton_dead_number = automata_number_of + 2

        graph = nx.Graph()

        # declare all graph edges between vertices
        graph_edges = [(0,3), (0,6), (0,8),
                       (1,2), (1,5), (1,6),
                       (2,3), (2,6),
                       (3,6),
                       (4,5), (4,7), (4,10),
                       (5,7), (5,8), (5,9), (5,10),
                       (6,8),
                       (7,9),
                       (8,9)]

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
        df_pop = pd.read_csv('../../../data/population.csv')

        initial_susceptible = []
        initial_asymptomatic = []

        # instantiate host objects
        for index, data in df_pop.iterrows():
            number = int(data['number'])
            age = data['age']
            sex = data['sex']
            health = data['health']
            state = int(data['state'])
            district = int(data['district'])
            host = Host(number, age, sex, health, state, district)
            # add host to automaton
            location = self.automata[district].setHost(host)
            # index host cell and automaton in array
            self.locations[number][0] = location[0]
            self.locations[number][1] = location[1]
            self.locations[number][2] = district
            if state == 0:
                attributes = [age, sex, health, district]
                initial_susceptible.append(attributes)
            elif state == 2:
                attributes = [age, sex, health, district]
                initial_asymptomatic.append(attributes)
            update = "\rBuilding hosts: " + str(number)
            print(update, end="")

        self.report_initial.append(initial_susceptible)
        self.report_initial.append(initial_asymptomatic)

    # move host to new automaton
    def changeAutomaton(self, host, automaton_number):
        x, y = self.automata[automaton_number].setHost(host)
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
        x, y, automaton = self.getPositions(host_number)
        self.automata[automaton].removeHost(x, y)
        self.isolation_tank[host_number][0] = host
        self.setPositions(host_number, 0, 0, self.automaton_isolation_number)

    def endIsolation(self, host_number):
        host = self.isolation_tank[host_number][0]
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

        self.setPositions(host_number, 0, 0, self.automaton_dead_number)
