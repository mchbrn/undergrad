from automata import Automata 
from new_hosts import generate_hosts
from report import Report
from copy import deepcopy
from datetime import datetime
from random import random
from random import randrange
from random import seed
import gym
from gym import error, spaces, utils
from gym.utils import seeding
import math
import numpy as np
import pandas as pd

class Simulation(gym.Env):
    def __init__(self, automata_number_of, hosts_number_of, days_total, moves):
        super(Simulation, self).__init__()
        # set gym variables
        # 11 automata that may be locked (1) or unlocked (0) reprepresented as a decimal value and later converted to an 11 bit binary number
        # wanted to use a Box space here but dqn required discrete action space
        self.action_space = spaces.Discrete(2048)
        # agent observes last week's lockdown status and number of cases of the automata
        # list #1 in low and high refer to unlocked or locked automata
        # list #2 in low and high refer to minimum and maximum number of cases in automata
        self.observation_space = spaces.Box(low=np.array([[0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0]]), high=np.array([[1,1,1,1,1,1,1,1,1,1,1], [344,216,181,162,151,149,146,145,144,139,117]]), dtype='int16')
        # minimum reward for if all 11 automata are locked and all hosts are infected
        # maximum for no lockdowns or cases
        self.reward_range = (0,22)
        # a step is equal to 1 week

        # set envrioment variables
        self.automata_number_of = automata_number_of
        self.hosts_number_of = hosts_number_of
        self.days_total = days_total
        self.weeks_total = int(days_total / 7)
        self.moves = moves
        self.report = Report(self.weeks_total)

        # set simulation variables
        self.steps = 0
        self.day = 0
        self.episode_number = 1
        self.done = False

    def step(self, action):
        self.takeAction(action)

        # run a week of the simulation
        self.run()

        # maxium reward
        reward = 22

        observation = self.report.getObservation(self.steps)
        automata_lockdowns, automata_cases = observation[0]

        # discount reward for every lockdown the agent executes
        for lockdown in automata_lockdowns:
            # if lockded (1) minus 1, if unlocked (0) minus 0
            reward -= lockdown

        # discount reward for every new case
        for cases in automata_cases:
            reward -= cases * 0.100722

        self.steps += 1

        # reset simulation
        if self.steps == self.weeks_total:
            self.report.makeReports()
            self.done = True

        return observation, reward, self.done, {}

    # reset environment every 52 weeks
    def reset(self):
        print("\n")
        print("------Episode " + str(self.episode_number) + "------")

        self.episode_number += 1
        # instantiate new automata with same hosts but different infections
        self.simulation = Automata(self.automata_number_of, self.hosts_number_of)
        # instantiate new report
        self.report = Report(self.weeks_total)

        # initialise report
        susceptible, cases_asymptomatic = self.simulation.report_initial
        self.report.initialise(susceptible, cases_asymptomatic)

        # reset simulation variables
        self.steps = 0
        self.day = 0
        self.done = False

        return self.nextObservation(0)

    def nextObservation(self, day):
        day += 1
        week = int(day / 7)
        observation = self.report.getObservation(week)
        return observation

    def takeAction(self, action):
        decimal = action

        binary = np.zeros((self.automata_number_of), dtype='int8')

        # convert decimal action into binary where each bit represents locking (1) or unlocking (0) the automaton whose number matches the bit's index
        for bit in range(len(binary)):
            if decimal % 2 == 1:
                binary[bit] = 1

        binary = np.flip(binary)

        for index, lockdown in enumerate(binary):
            if lockdown == 1:
                self.simulation.automata[index].lock()
                self.report.setLockdowns(index, self.day)
            else:
                self.simulation.automata[index].unlock()

    def run(self):
        # 7 days in a week
        for i in range(7):
            update_01= "\rDay: " + str(self.day + 1)
            print(update_01, end="")
            # however many moves in a day
            for j in range(self.moves):
                # animate cells
                for k in range(self.simulation.hosts_number_of):
                    x_current, y_current, automaton_number_current = self.simulation.getPositions(k)

                    # host is dead, skip to next host
                    if automaton_number_current == self.simulation.automaton_dead_number:
                        continue
                    # host is in self-isolation
                    elif automaton_number_current == self.simulation.automaton_isolation_number:
                        host = self.simulation.isolation_tank[k][0]
                    # host is in automata
                    else:
                        host = self.simulation.automata[automaton_number_current].getHost(x_current, y_current)
                        # lockdown implementation
                        if self.simulation.automata[automaton_number_current].locked == True:
                            seed()
                            chance_of_movement = random()

                            # only allow 1% of hosts to move during a lockdown
                            if chance_of_movement > 0.99:
                                pass
                            else:
                                continue

                    host_number = host.number
                    host_home = host.home
                    host_state = host.state
                    host_symptomatic = host.symptomatic
                    host_self_isolating = host.self_isolating
                    host_counter = host.counter
                    host_threshold = host.threshold
                    host_attributes = host.getAttributes()
                    if host_self_isolating:
                        host_attributes.append(host_home)
                    else:
                        host_attributes.append(automaton_number_current)
                    host_is_home = host_home == automaton_number_current
                    is_host_dead = False

                    #
                    # CHANGE STATES
                    #
                    if host_state == 0:
                        pass
                    # exposed -> infected
                    elif host_state == 1 and host_counter == 2:
                        host.setState(is_host_dead)

                        seed()
                        chance_of_symptoms = random()

                        if chance_of_symptoms > host_threshold:
                            host.symptomatic = True
                            self.report.setCaseSymptomatic(host_attributes, self.day)
                        else:
                            host.symptomatic = False
                            self.report.setCaseAsymptomatic(host_attributes, self.day)
                    # infected -> recovered/removed
                    elif host_state == 2 and host_counter > 2:
                        # host has recovered after 4 weeks
                        if host_counter == 28:
                            host.setState(is_host_dead)
                            self.report.setRecovery(host_attributes, self.day)
                            if host_self_isolating:
                                self.simulation.endIsolation(host.number)
                        elif host_symptomatic:
                            seed()
                            chance_of_death = random()

                            # remove host from simulation
                            if chance_of_death > host_threshold:
                                if host_self_isolating:
                                    self.simulation.terminateHost(host_number, True)
                                else:
                                    self.simulation.terminateHost(host_number, False)
                                is_host_dead = True
                                host.setState(is_host_dead)
                                self.report.setDeath(host_attributes, self.day)
                                continue

                            if host_self_isolating == False:
                                if host_counter == 3:
                                    self.report.setSelfIsolation(host_attributes, self.day)
                                    self.simulation.startIsolation(host, host_number)
                                    continue
                    # recovered host loses immunity after 12 weeks
                    elif host_state == 3 and host_counter == 84:
                        host.setState(is_host_dead)
                        self.report.setSusceptible(host_attributes, self.day)

                    #
                    # MOVE HOSTS
                    #
                    if not host_self_isolating and host.state > -1:
                        seed()
                        probability_change_automaton = random()
                        # send host home if away
                        if host_is_home == False and probability_change_automaton >= 0.5:
                            # home automaton is at capacity, move host around current automaton
                            if self.simulation.automata[host_home].atCapacity() or self.simulation.automata[host_home].locked:
                                x_new, y_new = self.simulation.automata[automaton_number_current].move(x_current, y_current)
                                self.simulation.setPositions(k, x_new, y_new, automaton_number_current)
                                # if host is infected
                                if host_state == 2:
                                    # transmit virus
                                    infections = self.simulation.automata[automaton_number_current].transmit(x_new, y_new)
                                    # record exposed hosts
                                    for infection in infections:
                                        self.report.setExposed(infection, self.day)
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
                                        self.report.setExposed(infection, self.day)
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
                                    if self.simulation.automata[automaton_number_new].atCapacity() or self.simulation.automata[automaton_number_new].locked:
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
                                                self.report.setExposed(infection, self.day)
                                        break
                                # all neighbouring automata are at capacity or locked, move host around current automaton
                                else:
                                    x_new, y_new = self.simulation.automata[automaton_number_current].move(x_current, y_current)
                                    self.simulation.setPositions(k, x_new, y_new, automaton_number_current)
                                    # if host is infected
                                    if host_state == 2:
                                        # transmit virus
                                        infections = self.simulation.automata[automaton_number_current].transmit(x_new, y_new)
                                        # record exposed hosts
                                        for infection in infections:
                                            self.report.setExposed(infection, self.day)
                                    break
                        # move host around current automaton
                        else:
                            x_new, y_new = self.simulation.automata[automaton_number_current].move(x_current, y_current)
                            self.simulation.setPositions(k, x_new, y_new, automaton_number_current)
                            # if host is infected
                            if host_state == 2:
                                # transmit virus
                                infections = self.simulation.automata[automaton_number_current].transmit(x_new, y_new)
                                # record exposed hosts
                                for infection in infections:
                                    self.report.setExposed(infection, self.day)

                    # if a day has passed, increment host counter
                    if j == self.moves - 1:
                        host.setCounter()
            
            # if a week has passed, import new hosts
            if (i + 1) % 7 == 0:
                self.importHosts(self.day)

            self.day += 1

    def importHosts(self, days):
        seed()
        number_of_hosts = random()
        number_of_hosts = number_of_hosts * 10
        number_of_hosts = round(number_of_hosts , 0)
        number_of_hosts = int(number_of_hosts)
        hosts = generate_hosts(number_of_hosts, self.simulation.hosts_number_of)

        locations = []
        
        # add imported hosts to their automata and save locations
        for host in hosts:
            x, y = self.simulation.changeAutomaton(host, host.home)
            location = [x, y, host.home]
            locations.append(location)

            attributes = host.getAttributes()
            attributes.append(host.home)
            self.report.setCaseAsymptomatic(attributes, days)

        if locations:
            # add locations of imported hosts to locations list
            self.simulation.locations = np.vstack((self.simulation.locations, locations))
            
            # make isolation tank bigger to accommodate imported hosts
            isolation_tank_extension = np.zeros((number_of_hosts, 1), dtype=object)
            self.simulation.isolation_tank = np.vstack((self.simulation.isolation_tank, isolation_tank_extension))

            # increase simulation's number of hosts variable
            self.simulation.hosts_number_of += number_of_hosts
