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
        self.automata_number_of = automata_number_of
        self.hosts_number_of = hosts_number_of
        self.counter = 1
        self.filename = "../../../data/" + str(datetime.now()) + ".txt"

    def run(self, days, steps):
        print(self.report.weekly_susceptible)
        for i in range(days):
            update_01= "\rDay: " + str(i + 1)
            print("\n")
            print(update_01, end="")
            print("\n")
            for j in range(steps):
                update_02 = "\rTime Step: " + str(j + 1)
                print(update_02, end="")
                # animate hosts
                for k in range(self.simulation.hosts_number_of):
                    x_current, y_current, automaton_number_current = self.simulation.getLocations(k)
                    host = self.simulation.automata[automaton_number_current].getHost(x_current, y_current)
                    host_home = host.home
                    host_state = host.state
                    host_symptomatic = host.symptomatic
                    host_counter = host.counter
                    host_threshold = host.threshold
                    host_attributes = host.getAttributes()
                    host_is_home = host_home == automaton_number_current
                    seed()
                    probability_change_automaton = random()

                    if host_state == 0:
                        pass
                    # exposed -> infected
                    elif host_state == 1 and host_counter == 2:
                        host.setState()

                        seed()
                        chance_of_symptoms = random()

                        if chance_of_symptoms > host_threshold:
                            host.symptomatic = True
                            report.setCaseSymptomatic(host_attributes, automaton_number_current)
                        else
                            host.symptomatic = False
                            report.setCaseAsymptomatic(host_attributes, automaton_number_current)
                    # infected -> recovered/removed
                    elif host_state == 2 and host_counter > 4:
                        # host has recovered after 3 weeks
                        if host_counter == 21:
                            host.setState()
                            report.setRecovery(host_attributes, automaton_number_current)
                        elif host_symptomatic:
                            seed()
                            chance_of_death = random()

                            # remove host from simulation
                            if chance_of_death > host_threshold:
                                report.setDeath(host_attributes, automaton_number_current)
                                self.simulation.removeHost(host_number)
                        # early asymptomatic -> recovered
                        else:
                            seed()
                            chance_of_recovery = random()

                            if chance_of_recovery > 0.8:
                                report.setRecovery(host_attributes, automaton_number_current)
                    elif host_state == 3 and host_counter <= 84:
                        host.setState()
                        report.setSusceptible(host_attributes, automaton_number_current)

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
                                    pass
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
                    if j == 19:
                        host.setCounter()

            # make weekly report
            if (i + 1) % 7 == 0:
                week_number = str(int((i + 1) / 7))
                with open(self.filename, "a") as f:
                    header = "-------Week " + week_number + "-------\n"
                    weekly_susceptible = "Susceptible: " + str(self.report.weekly_susceptible) + "\n"
                    weekly_exposed = "Exposed : " + str(self.report.weekly_exposed) + "\n"
                    weekly_cases = "Cases: " + str(self.report.weekly_cases) + "\n"
                    weekly_cases_symptomatic = "Symptomatic: " + str(self.report.weekly_cases_symptomatic) + "\n"
                    weekly_cases_asymptomatic = "Asymptomatic: " + str(self.report.weekly_cases_asymptomatic) + "\n"
                    weekly_self_isolating = "Self Isolating: " + str(self.report.weekly_self_isolating) + "\n"
                    weekly_recovered = "Recovered: " + str(self.report.weekly_recovered) + "\n"
                    weekly_deaths = "Deaths: " + str(self.report.weekly_deaths) + "\n"
                    weekly_lockdowns = "Lockdowns: " + str(self.report.weekly_lockdowns) + "\n"
                    f.write(header)
                    f.write(weekly_susceptible)
                    f.write(weekly_exposed)
                    f.write(weekly_cases)
                    f.write(weekly_cases_symptomatic)
                    f.write(weekly_cases_asymptomatic)
                    f.write(weekly_self_isolating)
                    f.write(weekly_recovered)
                    f.write(weekly_deaths)
                    f.write(weekly_lockdowns)

                self.report.newWeek()
