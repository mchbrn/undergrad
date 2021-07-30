from automata import Automata
from report import Report
from copy import deepcopy
from datetime import datetime
from random import random
from random import randrange
from random import seed
import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
import pandas as pd

class Simulation:
    def __init__(self, automata_number_of, hosts_number_of):
        self.simulation = Automata(automata_number_of, hosts_number_of)
        susceptible, cases_asymptomatic = self.simulation.report_initial
        self.report = Report()
        self.report.initialise(susceptible, cases_asymptomatic)
        self.counter = 1

    def run(self, days, steps):
        for i in range(days):
            update_01= "\rDay: " + str(i + 1)
            #print("\n")
            #print(update_01, end="")
            #print("\n")
            for j in range(steps):
                update_02 = "\rTime Step: " + str(j + 1)
                #print(update_02, end="")
                # animate hosts
                for k in range(self.simulation.hosts_number_of):
                    x_current, y_current, automaton_number_current = self.simulation.getPositions(k)
                    print("We think host is in: " + str([x_current, y_current]))

                    # host is in automata
                    if automaton_number_current >= 0 and automaton_number_current <= 9:
                        print("Host is not self-isolating")
                        host = self.simulation.automata[automaton_number_current].getHost(x_current, y_current)
                        print("The host in question: " + str(host))
                        host_number = host.number
                        host_home = host.home
                        host_state = host.state
                        host_symptomatic = host.symptomatic
                        host_counter = host.counter
                        host_threshold = host.threshold
                        host_attributes = host.getAttributes()
                        host_attributes.append(automaton_number_current)
                        host_is_home = host_home == automaton_number_current
                    # host is in self-isolation
                    elif automaton_number_current == 10:
                        print("Host is self-isolating")
                        host = self.simulation.isolation_tank[k][0]
                        print("The Host in question is: " + str(host))
                        host_number = host.number
                        host_home = host.home
                        host_state = host.state
                        host_symptomatic = host.symptomatic
                        host_counter = host.counter
                        host_threshold = host.threshold
                        host_attributes = host.getAttributes()
                        host_attributes.append(automaton_number_current)
                        host_is_home = host_home == automaton_number_current
                    # host is dead
                    elif automaton_number_current == 11:
                        continue

                    print("Host attributes: " + str(host_attributes))
                    print("Host state: " + str(host_state))

                    #
                    # CHANGE STATES
                    #
                    if host_state == 0:
                        pass
                    # exposed -> infected
                    elif host_state == 1 and host_counter == 2:
                        host.setState()

                        seed()
                        chance_of_symptoms = random()

                        if chance_of_symptoms > host_threshold:
                            host.symptomatic = True
                            self.report.setCaseSymptomatic(host_attributes, i)
                        else:
                            host.symptomatic = False
                            self.report.setCaseAsymptomatic(host_attributes, i)
                    # infected -> recovered/removed
                    elif host_state == 2 and host_counter > 2:
                        # host has recovered after 3 weeks
                        if host_counter == 21:
                            host.setState()
                            self.report.setRecovery(host_attributes, i)
                            if host.self_isolating:
                                self.simulation.endIsolation(host)
                        elif host_symptomatic:
                            seed()
                            chance_of_death = random()

                            # remove host from simulation
                            if chance_of_death > host_threshold:
                                if host.self_isolating:
                                    self.simulation.terminateHost(host_number, True)
                                else:
                                    self.simulation.terminateHost(host_number, False)
                                host.setState()
                                self.report.setDeath(host_attributes, i)
                            elif host_counter == 3:
                                self.simulation.startIsolation(host, host_number)
                        # early asymptomatic -> recovered
                        else:
                            # host has recovered after 3 weeks
                            if host_counter == 21:
                                host.setState()
                                self.report.setRecovery(host_attributes, i)
                            else:
                                seed()
                                chance_of_recovery = random()

                                if chance_of_recovery > 0.8:
                                    host.setState()
                                    self.report.setRecovery(host_attributes, i)
                    # recovered host loses immunity after 12 weeks
                    elif host_state == 3 and host_counter == 84:
                        host.setState()
                        self.report.setSusceptible(host_attributes, i)

                    #
                    # MOVE HOSTS
                    #
                    if not host.self_isolating:
                        seed()
                        probability_change_automaton = random()
                        # send host home if away
                        if host_is_home == False and probability_change_automaton > 0.5:
                            # home automaton is at capacity, move host around current automaton
                            if self.simulation.automata[host_home].atCapacity():
                                x_new, y_new = self.simulation.automata[automaton_number_current].move(x_current, y_current)
                                cell = [x_new, y_new]
                                cells_available, cells_empty = self.simulation.automata[automaton_number_current].getNeighbourhood(cell)
                                print("cells available")
                                for cell_a in cells_available:
                                    print(cell_a)
                                    x_a, y_a = cell_a
                                    print(self.simulation.automata[automaton_number_current].coordinates[x_a][y_a])

                                print("taken cells")
                                for cell_e in cells_empty:
                                    print(cell_e)
                                    x_e, y_e = cell_e
                                    print(self.simulation.automata[automaton_number_current].coordinates[x_e][y_e])

                                self.simulation.setPositions(k, x_new, y_new, automaton_number_current)
                                # if host is infected
                                if host_state == 2:
                                    # transmit virus
                                    infections = self.simulation.automata[automaton_number_current].transmit(x_new, y_new)
                                    # record exposed hosts
                                    for infection in infections:
                                        self.report.setExposed(infection, i)
                            else:
                                self.simulation.automata[automaton_number_current].removeHost(x_current, y_current)
                                x_new, y_new = self.simulation.changeAutomaton(host, host_home)
                                self.simulation.setPositions(k, x_new, y_new, host_home)
                                # if host is infected
                                if host_state == 2:
                                    # transmit virus
                                    infections = self.simulation.automata[host_home].transmit(x_new, y_new)
                                    # record exposed hosts
                                    for infection in infections:
                                        self.report.setExposed(infection, i)
                        # allow host to change automaton
                        elif probability_change_automaton <= 0.1:
                            edges = deepcopy(self.simulation.automata[automaton_number_current].getEdges())
                            edges_number_of = self.simulation.automata[automaton_number_current].getEdgesNumberOf()
                            while True:
                                if edges_number_of > 0:
                                    seed()
                                    edges_index = randrange(0, edges_number_of, 1)
                                    automaton_number_new = edges[edges_index]
                                    # automaton is at capacity, pop from list and try another
                                    if self.simulation.automata[automaton_number_new].atCapacity():
                                        edges_number_of -= 1
                                        edges.pop(edges_index)
                                    # automaton has space, remove host from current automaton and send to new
                                    else:
                                        self.simulation.automata[automaton_number_current].removeHost(x_current, y_current)
                                        x_new, y_new = self.simulation.changeAutomaton(host, automaton_number_new)
                                        self.simulation.setPositions(k, x_new, y_new, automaton_number_new)
                                        # if host is infected
                                        if host_state == 2:
                                            # transmit virus
                                            infections = self.simulation.automata[automaton_number_new].transmit(x_new, y_new)
                                            # record exposed hosts
                                            for infection in infections:
                                                self.report.setExposed(infection, i)
                                        break
                                # all neighbouring automata at capacity, move host around current automaton
                                else:
                                    x_new, y_new = self.simulation.automata[automaton_number_current].move(x_current, y_current)
                                    cell = [x_new, y_new]
                                    cells_available, cells_empty = self.simulation.automata[automaton_number_current].getNeighbourhood(cell)
                                    print("cells available")
                                    for cell_a in cells_available:
                                        print(cell_a)
                                        x_a, y_a = cell_a
                                        print(self.simulation.automata[automaton_number_current].coordinates[x_a][y_a])

                                    print("taken cells")
                                    for cell_e in cells_empty:
                                        print(cell_e)
                                        x_e, y_e = cell_e
                                        print(self.simulation.automata[automaton_number_current].coordinates[x_e][y_e])

                                    self.simulation.setLocations(k, x_new, y_new, automaton_number_current)
                                    # if host is infected
                                    if host_state == 2:
                                        # transmit virus
                                        infections = self.simulation.automata[automaton_number_current].transmit(x_new, y_new)
                                        # record exposed hosts
                                        for infection in infections:
                                            self.report.setExposed(infection, i)
                                    break
                        # move host around current automaton
                        else:
                            x_new, y_new = self.simulation.automata[automaton_number_current].move(x_current, y_current)
                            cell = [x_new, y_new]
                            cells_available, cells_empty = self.simulation.automata[automaton_number_current].getNeighbourhood(cell)
                            print("cells available")
                            for cell_a in cells_available:
                                print(cell_a)
                                x_a, y_a = cell_a
                                print(self.simulation.automata[automaton_number_current].coordinates[x_a][y_a])

                            print("taken cells")
                            for cell_e in cells_empty:
                                print(cell_e)
                                x_e, y_e = cell_e
                                print(self.simulation.automata[automaton_number_current].coordinates[x_e][y_e])

                            self.simulation.setPositions(k, x_new, y_new, automaton_number_current)
                            # if host is infected
                            if host_state == 2:
                                # transmit virus
                                infections = self.simulation.automata[automaton_number_current].transmit(x_new, y_new)
                                # record exposed hosts
                                for infection in infections:
                                    self.report.setExposed(infection, i)

                    # if a day has passed, increment host counter
                    if j == 19:
                        host.setCounter()

        self.report.makeReports()
