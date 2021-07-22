from automata import Automata
from report import Report
from copy import deepcopy
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
        self.report = Report()
        self.automata_number_of = automata_number_of
        self.hosts_number_of = hosts_number_of
        self.counter = 1

    def run(self, days, minutes):
        for i in range(days):
            update_01= "\rDay: " + str(i)
            print("\n")
            print(update_01, end="")
            print("\n")
            for j in range(minutes):
                update_02 = "\rTime Step: " + str(j)
                print(update_02, end="")
                # animate hosts
                for k in range(self.simulation.hosts_number_of):
                    x_current, y_current, automaton_number_current = self.simulation.getLocations(k)
                    host = self.simulation.automata[automaton_number_current].getHost(x_current, y_current)
                    host_home = host.getHome()
                    host_state = host.getState()
                    host_is_home = host_home == automaton_number_current
                    seed()
                    probability_change_automaton = random()
                    # send host home if away
                    if host_is_home == False and probability_change_automaton > 0.5:
                        # home automaton is at capacity, move host around current automaton
                        if self.simulation.automata[host_home].atCapacity():
                            x_new, y_new = self.simulation.automata[automaton_number_current].move(x_current, y_current)
                            self.simulation.setLocations(k, x_new, y_new, automaton_number_current)
                            # if host is infected
                            if host_state == 2:
                                infections = self.simulation.automata[automaton_number_current].transmit(x_new, y_new)
                                if infections:
                                    # add to report
                        else:
                            self.simulation.automata[automaton_number_current].removeHost(x_current, y_current)
                            x_new, y_new = self.simulation.changeAutomaton(host, host_home)
                            self.simulation.setLocations(k, x_new, y_new, host_home)
                            # if host is infected
                            if host_state == 2:
                                self.simulation.automata[host_home].transmit(x_new, y_new)
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
                                    self.simulation.setLocations(k, x_new, y_new, automaton_number_new)
                                    # if host is infected
                                    if host_state == 2:
                                        self.simulation.automata[automaton_number_new].transmit(x_new, y_new)
                                    break
                            # all neighbouring automata at capacity, move host around current automaton
                            else:
                                x_new, y_new = self.simulation.automata[automaton_number_current].move(x_current, y_current)
                                self.simulation.setLocations(k, x_new, y_new, automaton_number_current)
                                # if host is infected
                                if host_state == 2:
                                    self.simulation.automata[automaton_number_current].transmit(x_new, y_new)
                                break
                    # move host around current automaton
                    else:
                        x_new, y_new = self.simulation.automata[automaton_number_current].move(x_current, y_current)
                        self.simulation.setLocations(k, x_new, y_new, automaton_number_current)
                        # if host is infected
                        if host_state == 2:
                            self.simulation.automata[automaton_number_current].transmit(x_new, y_new)

                    # if a day has passed, increment host counter
                    if k % 19 == 0:
                        host.setCounter()
