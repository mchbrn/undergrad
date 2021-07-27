from abc import ABC, abstractmethod
import math
import numpy as np
import pandas as pd

class Report():
    def __init__(self):
        axes_age = np.zeros((52, 10), dtype='int16')
        axes_sex = np.zeros((52, 2), dtype='int16')
        axes_ethnicity = np.zeros((52, 5), dtype='int16')
        axes_health = np.zeros((52, 5) dtype='int16')
        axes_automaton = np.zeros((52, 10) dtype='int16')

        self.susceptible = pd.Series(np.zeros((52), dtype='int16'))
        self.susceptible_age = pd.DataFrame(axes_age)
        self.susceptible_sex = pd.DataFrame(axes_sex, columns=['m', 'f'])
        self.susceptible_ethnicity = pd.DataFrame(axes_ethnicity, columns=['we', 'an', 'bk', 'md', 'or'])
        self.susceptible_health = pd.DataFrame(axes_health)
        self.susceptible_automaton = pd.DataFrame(axes_automaton)

        self.cases = pd.Series(np.zeros((52), dtype='int16'))
        self.cases_age = pd.DataFrame(axes_age)
        self.cases_sex = pd.DataFrame(axes_sex, columns=['m', 'f'])
        self.cases_ethnicity = pd.DataFrame(axes_ethnicity, columns=['we', 'an', 'bk', 'md', 'or'])
        self.cases_health = pd.DataFrame(axes_health)
        self.cases_automaton = pd.DataFrame(axes_automaton)

        self.cases_symptomatic = pd.Series(np.zeros((52), dtype='int16'))
        self.cases_symptomatic_age = pd.DataFrame(axes_age)
        self.cases_symptomatic_sex = pd.DataFrame(axes_sex, columns=['m', 'f'])
        self.cases_symptomatic_ethnicity = pd.DataFrame(axes_ethnicity, columns=['we', 'an', 'bk', 'md', 'or'])
        self.cases_symptomatic_health = pd.DataFrame(axes_health)
        self.cases_symptomatic_automaton = pd.DataFrame(axes_automaton)

        self.cases_asymptomatic = pd.Series(np.zeros((52), dtype='int16'))
        self.cases_asymptomatic_age = pd.DataFrame(axes_age)
        self.cases_asymptomatic_sex = pd.DataFrame(axes_sex, columns=['m', 'f'])
        self.cases_asymptomatic_ethnicity = pd.DataFrame(axes_ethnicity, columns=['we', 'an', 'bk', 'md', 'or'])
        self.cases_asymptomatic_health = pd.DataFrame(axes_health)
        self.cases_asymptomatic_automaton = pd.DataFrame(axes_automaton)

        self.self_isolating = pd.Series(np.zeros((52), dtype='int16'))
        self.self_isolating_age = pd.DataFrame(axes_age)
        self.self_isolating_sex = pd.DataFrame(axes_sex, columns=['m', 'f'])
        self.self_isolating_ethnicity = pd.DataFrame(axes_ethnicity, columns=['we', 'an', 'bk', 'md', 'or'])
        self.self_isolating_health = pd.DataFrame(axes_health)
        self.self_isolating_automaton = pd.DataFrame(axes_automaton)

        self.recovered = pd.Series(np.zeros((52), dtype='int16'))
        self.recovered_age = pd.DataFrame(axes_age)
        self.recovered_sex = pd.DataFrame(axes_sex, columns=['m', 'f'])
        self.recovered_ethnicity = pd.DataFrame(axes_ethnicity, columns=['we', 'an', 'bk', 'md', 'or'])
        self.recovered_health = pd.DataFrame(axes_health)
        self.recovered_automaton = pd.DataFrame(axes_automaton)

        self.deaths = pd.Series(np.zeros((52), dtype='int16'))
        self.deaths_age = pd.DataFrame(axes_age)
        self.deaths_sex = pd.DataFrame(axes_sex, columns=['m', 'f'])
        self.deaths_ethnicity = pd.DataFrame(axes_ethnicity, columns=['we', 'an', 'bk', 'md', 'or'])
        self.deaths_health = pd.DataFrame(axes_health)
        self.deaths_automaton = pd.DataFrame(axes_automaton)

        self.lockdowns = pd.Series(np.zeros((52), dtype='int16'))
        self.lockdowns_age = pd.DataFrame(axes_age)
        self.lockdowns_sex = pd.DataFrame(axes_sex, columns=['m', 'f'])
        self.locdowns_ethnicity = pd.DataFrame(axes_ethnicity, columns=['we', 'an', 'bk', 'md', 'or'])
        self.lockdowns_health = pd.DataFrame(axes_health)
        self.lockdowns_automaton = pd.DataFrame(axes_automaton)

    def initialise(self, susceptible, cases_asymptomatic):
        self.setSusceptible(susceptible, 0)
        self.setCasesAsymptomatic(cases_asymptomatic, 0)

    def setSusceptible(self, attributes, days):
        week = math.floor(days / 7)
        age, sex, ethnicity, health, automaton = attributes
        self.susceptible[week] += 1
        self.susceptible_age[age][week] += 1
        self.susceptible_sex[sex][week] += 1
        self.susceptible_ethnicity[ethnicity][week] += 1
        self.susceptible_health[health][week] += 1
        self.susceptible_automaton[automaton][week] += 1

    def setExposed(self, attributes, days):
        week = math.floor(days / 7)
        age, sex, ethnicity, health, automaton = attributes
        self.exposed[week] += 1
        self.exposed_age[age][week] += 1
        self.exposed_sex[sex][week] += 1
        self.exposed_ethnicity[ethnicity][week] += 1
        self.exposed_health[health][week] += 1
        self.exposed_automaton[automaton][week] += 1

    @abstractmethod
    def setCase(self, attributes, week):
        age, sex, ethnicity, health, automaton = attributes
        self.cases[week] += 1
        self.cases_age[age][week] += 1
        self.cases_sex[sex][week] += 1
        self.cases_ethnicity[ethnicity][week] += 1
        self.cases_health[health][week] += 1
        self.cases_automaton[automaton][week] += 1

    def setCaseSymptomatic(self, attributes, days):
        week = math.floor(days / 7)
        self.setCase(attributes, week)
        age, sex, ethnicity, health, automaton = attributes
        self.cases_symptomatic[week] += 1
        self.cases_symptomatic_age[age][week] += 1
        self.cases_symptomatic_sex[sex][week] += 1
        self.cases_symptomatic_ethnicity[ethnicity][week] += 1
        self.cases_symptomatic_health[health][week] += 1
        self.cases_symptomatic_automaton[automaton][week] += 1

    def setCaseAsymptomatic(self, attributes, days):
        week = math.floor(days / 7)
        self.setCase(attributes, week)
        age, sex, ethnicity, health, automaton = attributes
        self.cases_asymptomatic[week] += 1
        self.cases_asymptomatic_age[age][week] += 1
        self.cases_asymptomatic_sex[sex][week] += 1
        self.cases_asymptomatic_ethnicity[ethnicity][week] += 1
        self.cases_asymptomatic_health[health][week] += 1
        self.cases_asymptomatic_automaton[automaton][week] += 1
            
    def setSelfIsolation(self, attributes, days):
        week = math.floor(days / 7)
        age, sex, ethnicity, health, automaton = attributes
        self.self_isolating[week] += 1
        self.self_isolating_age[age][week] += 1
        self.self_isolating_sex[sex][week] += 1
        self.self_isolating_ethnicity[ethnicity][week] += 1
        self.self_isolating_health[health][week] += 1
        self.self_isolating_automaton[automaton][week] += 1

    def setRecovery(self, attributes, days):
        week = math.floor(days / 7)
        age, sex, ethnicity, health, automaton = attributes
        self.recovered[week] += 1
        self.recovered_age[age][week] += 1
        self.recovered_sex[sex][week] += 1
        self.recovered_ethnicity[ethnicity][week] += 1
        self.recovered_health[health][week] += 1
        self.recovered_automaton[automaton][week] += 1

    def setDeath(self, attributes, days):
        age, sex, ethnicity, health, automaton = attributes
        week = math.floor(days / 7)
        self.deaths[week] += 1
        self.deaths_age[age][week] += 1
        self.deaths_sex[sex][week] += 1
        self.deaths_ethnicity[ethnicity][week] += 1
        self.deaths_health[health][week] += 1
        self.deaths_automaton[automaton][week] += 1

    def setLockdowns(self, lockdowns):
        pass
