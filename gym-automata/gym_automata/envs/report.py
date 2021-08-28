from abc import ABC, abstractmethod
from copy import deepcopy
from datetime import datetime
import math
import numpy as np
import pandas as pd
import os

class Report():
    def __init__(self, weeks):
        datetime_now = datetime.now()
        self.now = datetime_now.strftime("%d-%m-%Y-%H-%M-%S")

        axes_age = np.zeros((weeks, 10), dtype='int16')
        axes_sex = np.zeros((weeks, 2), dtype='int16')
        axes_health = np.zeros((weeks, 5), dtype='int16')
        axes_automaton = np.zeros((weeks, 11), dtype='int16')

        self.susceptible = pd.Series(np.zeros((weeks), dtype='int16'))
        self.susceptible_age = pd.DataFrame(deepcopy(axes_age))
        self.susceptible_sex = pd.DataFrame(deepcopy(axes_sex), columns=['m', 'f'])
        self.susceptible_health = pd.DataFrame(deepcopy(axes_health))
        self.susceptible_automaton = pd.DataFrame(deepcopy(deepcopy(axes_automaton)))

        self.exposed = pd.Series(np.zeros((weeks), dtype='int16'))
        self.exposed_age = pd.DataFrame(deepcopy(axes_age))
        self.exposed_sex = pd.DataFrame(deepcopy(axes_sex), columns=['m', 'f'])
        self.exposed_health = pd.DataFrame(deepcopy(axes_health))
        self.exposed_automaton = pd.DataFrame(deepcopy(axes_automaton))

        self.cases = pd.Series(np.zeros((weeks), dtype='int16'))
        self.cases_age = pd.DataFrame(deepcopy(axes_age))
        self.cases_sex = pd.DataFrame(deepcopy(axes_sex), columns=['m', 'f'])
        self.cases_health = pd.DataFrame(deepcopy(axes_health))
        self.cases_automaton = pd.DataFrame(deepcopy(axes_automaton))

        self.cases_symptomatic = pd.Series(np.zeros((weeks), dtype='int16'))
        self.cases_symptomatic_age = pd.DataFrame(deepcopy(axes_age))
        self.cases_symptomatic_sex = pd.DataFrame(deepcopy(axes_sex), columns=['m', 'f'])
        self.cases_symptomatic_health = pd.DataFrame(deepcopy(axes_health))
        self.cases_symptomatic_automaton = pd.DataFrame(deepcopy(axes_automaton))

        self.cases_asymptomatic = pd.Series(np.zeros((weeks), dtype='int16'))
        self.cases_asymptomatic_age = pd.DataFrame(deepcopy(axes_age))
        self.cases_asymptomatic_sex = pd.DataFrame(deepcopy(axes_sex), columns=['m', 'f'])
        self.cases_asymptomatic_health = pd.DataFrame(deepcopy(axes_health))
        self.cases_asymptomatic_automaton = pd.DataFrame(deepcopy(axes_automaton))

        self.self_isolating = pd.Series(np.zeros((weeks), dtype='int16'))
        self.self_isolating_age = pd.DataFrame(deepcopy(axes_age))
        self.self_isolating_sex = pd.DataFrame(deepcopy(axes_sex), columns=['m', 'f'])
        self.self_isolating_health = pd.DataFrame(deepcopy(axes_health))
        self.self_isolating_automaton = pd.DataFrame(deepcopy(axes_automaton))

        self.recovered = pd.Series(np.zeros((weeks), dtype='int16'))
        self.recovered_age = pd.DataFrame(deepcopy(axes_age))
        self.recovered_sex = pd.DataFrame(deepcopy(axes_sex), columns=['m', 'f'])
        self.recovered_health = pd.DataFrame(deepcopy(axes_health))
        self.recovered_automaton = pd.DataFrame(deepcopy(axes_automaton))

        self.deaths = pd.Series(np.zeros((weeks), dtype='int16'))
        self.deaths_age = pd.DataFrame(deepcopy(axes_age))
        self.deaths_sex = pd.DataFrame(deepcopy(axes_sex), columns=['m', 'f'])
        self.deaths_health = pd.DataFrame(deepcopy(axes_health))
        self.deaths_automaton = pd.DataFrame(deepcopy(axes_automaton))

        #self.lockdowns = pd.Series(np.zeros((weeks), dtype='int16'))
        #self.lockdowns_age = pd.DataFrame(deepcopy(axes_age))
        #self.lockdowns_sex = pd.DataFrame(deepcopy(axes_sex), columns=['m', 'f'])
        #self.lockdowns_health = pd.DataFrame(deepcopy(axes_health))
        self.lockdowns_automaton = pd.DataFrame(deepcopy(axes_automaton))

    def initialise(self, susceptible, cases_asymptomatic):
        for attributes in susceptible:
            self.setSusceptible(attributes, 0)
        
        for attributes in cases_asymptomatic:
            self.setCaseAsymptomatic(attributes, 0)

        self.makeDirs()

    def getObservation(self, day):
        day += 1
        week = int(day / 7)
        return np.array([[self.lockdowns_automaton[week], self.cases_automaton[week]]])

    def makeDirs(self):
        os.mkdir('../../../data/simulations/' + self.now)
        os.mkdir('../../../data/simulations/' + self.now + '/susceptible')
        os.mkdir('../../../data/simulations/' + self.now + '/exposed')
        os.mkdir('../../../data/simulations/' + self.now + '/cases')
        os.mkdir('../../../data/simulations/' + self.now + '/cases/symptomatic')
        os.mkdir('../../../data/simulations/' + self.now + '/cases/asymptomatic')
        os.mkdir('../../../data/simulations/' + self.now + '/self-isolating')
        os.mkdir('../../../data/simulations/' + self.now + '/recovered')
        os.mkdir('../../../data/simulations/' + self.now + '/deaths')
        os.mkdir('../../../data/simulations/' + self.now + '/lockdowns')

    def setSusceptible(self, attributes, day):
        day += 1
        week = math.floor(day / 7)
        age, sex, health, automaton = attributes
        self.susceptible[week] += 1
        self.susceptible_age[age][week] += 1
        self.susceptible_sex[sex][week] += 1
        self.susceptible_health[health][week] += 1
        self.susceptible_automaton[automaton][week] += 1

    def setExposed(self, attributes, day):
        day += 1
        week = math.floor(day / 7)
        age, sex, health, automaton = attributes
        self.exposed[week] += 1
        self.exposed_age[age][week] += 1
        self.exposed_sex[sex][week] += 1
        self.exposed_health[health][week] += 1
        self.exposed_automaton[automaton][week] += 1

    @abstractmethod
    def setCase(self, attributes, week):
        age, sex, health, automaton = attributes
        self.cases[week] += 1
        self.cases_age[age][week] += 1
        self.cases_sex[sex][week] += 1
        self.cases_health[health][week] += 1
        self.cases_automaton[automaton][week] += 1

    def setCaseSymptomatic(self, attributes, day):
        day += 1
        week = math.floor(day / 7)
        self.setCase(attributes, week)
        age, sex, health, automaton = attributes
        self.cases_symptomatic[week] += 1
        self.cases_symptomatic_age[age][week] += 1
        self.cases_symptomatic_sex[sex][week] += 1
        self.cases_symptomatic_health[health][week] += 1
        self.cases_symptomatic_automaton[automaton][week] += 1

    def setCaseAsymptomatic(self, attributes, day):
        day += 1
        week = math.floor(day / 7)
        self.setCase(attributes, week)
        age, sex, health, automaton = attributes
        self.cases_asymptomatic[week] += 1
        self.cases_asymptomatic_age[age][week] += 1
        self.cases_asymptomatic_sex[sex][week] += 1
        self.cases_asymptomatic_health[health][week] += 1
        self.cases_asymptomatic_automaton[automaton][week] += 1
            
    def setSelfIsolation(self, attributes, day):
        day += 1
        week = math.floor(days / 7)
        age, sex, health, automaton = attributes
        self.self_isolating[week] += 1
        self.self_isolating_age[age][week] += 1
        self.self_isolating_sex[sex][week] += 1
        self.self_isolating_health[health][week] += 1
        self.self_isolating_automaton[automaton][week] += 1

    def setRecovery(self, attributes, day):
        day += 1
        week = math.floor(day / 7)
        age, sex, health, automaton = attributes
        self.recovered[week] += 1
        self.recovered_age[age][week] += 1
        self.recovered_sex[sex][week] += 1
        self.recovered_health[health][week] += 1
        self.recovered_automaton[automaton][week] += 1

    def setDeath(self, attributes, day):
        day += 1
        age, sex, health, automaton = attributes
        week = math.floor(day / 7)
        self.deaths[week] += 1
        self.deaths_age[age][week] += 1
        self.deaths_sex[sex][week] += 1
        self.deaths_health[health][week] += 1
        self.deaths_automaton[automaton][week] += 1

    def setLockdowns(self, automaton, day):
        day += 1
        week = math.floor(days / 7)
        self.lockdowns_automaton[automaton][week] = 1

    def makeReports(self):
        path = '../../../data/simulations/' + self.now +'/susceptible/total.csv'
        self.susceptible.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now +'/susceptible/age.csv'
        self.susceptible_age.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now +'/susceptible/sex.csv'
        self.susceptible_sex.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now +'/susceptible/health.csv'
        self.susceptible_health.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now +'/susceptible/automaton.csv'
        self.susceptible_automaton.to_csv(path, index=False)

        path = '../../../data/simulations/' + self.now +'/exposed/total.csv'
        self.exposed.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now +'/exposed/age.csv'
        self.exposed_age.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now +'/exposed/sex.csv'
        self.exposed_sex.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now +'/exposed/health.csv'
        self.exposed_health.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now +'/exposed/automaton.csv'
        self.exposed_automaton.to_csv(path, index=False)

        path = '../../../data/simulations/' + self.now +'/cases/total.csv'
        self.cases.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now +'/cases/age.csv'
        self.cases_age.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now +'/cases/sex.csv'
        self.cases_sex.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now + '/cases/health.csv'
        self.cases_health.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now + '/cases/automaton.csv'
        self.cases_automaton.to_csv(path, index=False)

        path = '../../../data/simulations/' + self.now +'/cases/symptomatic/total.csv'
        self.cases_symptomatic.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now +'/cases/symptomatic/age.csv'
        self.cases_symptomatic_age.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now +'/cases/symptomatic/sex.csv'
        self.cases_symptomatic_sex.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now + '/cases/symptomatic/health.csv'
        self.cases_symptomatic_health.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now + '/cases/symptomatic/automaton.csv'
        self.cases_symptomatic_automaton.to_csv(path, index=False)

        path = '../../../data/simulations/' + self.now +'/cases/asymptomatic/total.csv'
        self.cases_asymptomatic.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now +'/cases/asymptomatic/age.csv'
        self.cases_asymptomatic_age.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now +'/cases/asymptomatic/sex.csv'
        self.cases_asymptomatic_sex.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now + '/cases/asymptomatic/health.csv'
        self.cases_asymptomatic_health.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now + '/cases/asymptomatic/automaton.csv'
        self.cases_asymptomatic_automaton.to_csv(path, index=False)

        path = '../../../data/simulations/' + self.now +'/self-isolating/total.csv'
        self.self_isolating.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now +'/self-isolating/age.csv'
        self.self_isolating_age.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now +'/self-isolating/sex.csv'
        self.self_isolating_sex.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now + '/self-isolating/health.csv'
        self.self_isolating_health.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now + '/self-isolating/automaton.csv'
        self.self_isolating_automaton.to_csv(path, index=False)

        path = '../../../data/simulations/' + self.now +'/recovered/total.csv'
        self.recovered.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now +'/recovered/age.csv'
        self.recovered_age.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now +'/recovered/sex.csv'
        self.recovered_sex.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now + '/recovered/health.csv'
        self.recovered_health.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now + '/recovered/automaton.csv'
        self.recovered_automaton.to_csv(path, index=False)

        path = '../../../data/simulations/' + self.now +'/deaths/total.csv'
        self.deaths.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now +'/deaths/age.csv'
        self.deaths_age.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now +'/deaths/sex.csv'
        self.deaths_sex.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now + '/deaths/health.csv'
        self.deaths_health.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now + '/deaths/automaton.csv'
        self.deaths_automaton.to_csv(path, index=False)

        #path = '../../../data/simulations/' + self.now +'/lockdowns/total.csv'
        #self.lockdowns.to_csv(path, index=False)
        #path = '../../../data/simulations/' + self.now +'/lockdowns/age.csv'
        #self.lockdowns_age.to_csv(path, index=False)
        #path = '../../../data/simulations/' + self.now +'/lockdowns/sex.csv'
        #self.lockdowns_sex.to_csv(path, index=False)
        #path = '../../../data/simulations/' + self.now + '/lockdowns/health.csv'
        #self.lockdowns_health.to_csv(path, index=False)
        path = '../../../data/simulations/' + self.now + '/lockdowns/automaton.csv'
        self.lockdowns_automaton.to_csv(path, index=False)
