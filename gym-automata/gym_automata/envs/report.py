from abc import ABC, abstractmethod
import pandas as pd

class Report():
    def __init__(self):
        # grand totals
        self.susceptible_age = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])
        self.susceptible_sex = pd.DataFrame({'m': 0, 'f': 0}, index=[0])
        self.susceptible_ethnicity = pd.DataFrame({'we': 0, 'an': 0, 'bk': 0, 'md': 0, 'or': 0}, index=[0])
        self.susceptible_health = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0}, index=[0])
        self.susceptible_automaton = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index=[0])

        self.cases_age = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index=[0])
        self.cases_sex = pd.DataFrame({'m': 0, 'f': 0}, index[0])
        self.cases_ethnicity = pd.DataFrame({'we': 0, 'an': 0, 'bk': 0, 'md': 0, 'or': 0}, index=[0])
        self.cases_health = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0}, index=[0])
        self.cases_automaton = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index=[0])

        self.cases_symptomatic_age = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index=[0])
        self.cases_symptomatic_sex = pd.DataFrame({'m': 0, 'f': 0}, index=[0])
        self.cases_symptomatic_ethnicity = pd.DataFrame({'we': 0, 'an': 0, 'bk': 0, 'md': 0, 'or': 0}, index=[0])
        self.cases_symptomatic_health = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0}, index[0])
        self.cases_symptomatic_automaton = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])

        self.cases_asymptomatic_age = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])
        self.cases_asymptomatic_sex = pd.DataFrame({'m': 0, 'f': 0}, index[0])
        self.cases_asymptomatic_ethnicity = pd.DataFrame({'we': 0, 'an': 0, 'bk': 0, 'md': 0, 'or': 0}, index[0])
        self.cases_asymptomatic_health = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0}, index[0])
        self.cases_asymptomatic_automaton = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])

        self.self_isolating_age = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])
        self.self_isolating_sex = pd.DataFrame({'m': 0, 'f': 0}, index[0])
        self.self_isolating_ethnicity = pd.DataFrame({'we': 0, 'an': 0, 'bk': 0, 'md': 0, 'or': 0}, index[0])
        self.self_isolating_health = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0}, index=[0])
        self.self_isolating_automaton = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])

        self.recovered_age = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])
        self.recovered_sex = pd.DataFrame({'m': 0, 'f': 0}, index[0])
        self.recovered_ethnicity = pd.DataFrame({'we': 0, 'an': 0, 'bk': 0, 'md': 0, 'or': 0}, index[0])
        self.recovered_health = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0}, index=[0])
        self.recovered_automaton = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])

        self.deaths_age = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])
        self.deaths_sex = pd.DataFrame({'m': 0, 'f': 0}, index[0])
        self.deaths_ethnicity = pd.DataFrame({'we': 0, 'an': 0, 'bk': 0, 'md': 0, 'or': 0}, index[0])
        self.deaths_health = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0}, index=[0])
        self.deaths_automaton = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])

        self.lockdowns_age = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])
        self.lockdowns_sex = pd.DataFrame({'m': 0, 'f': 0}, index[0])
        self.locdowns_ethnicity = pd.DataFrame({'we': 0, 'an': 0, 'bk': 0, 'md': 0, 'or': 0}, index[0])
        self.lockdowns_health = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0}, index=[0])
        self.lockdowns_automaton = pd.DataFrame({0: False, 1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False}, index[0])

        # weekly totals
        self.weekly_susceptible_age = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])
        self.weekly_susceptible_sex = pd.DataFrame({'m': 0, 'f': 0}, index[0])
        self.weekly_susceptible_ethnicity = pd.DataFrame({'we': 0, 'an': 0, 'bk': 0, 'md': 0, 'or': 0}, index[0])
        self.weekly_susceptible_health = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0}, index=[0])
        self.weekly_susceptible_automaton = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])

        self.weekly_cases_age = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])
        self.weekly_cases_sex = pd.DataFrame({'m': 0, 'f': 0}, index[0])
        self.weekly_cases_ethnicity = pd.DataFrame({'we': 0, 'an': 0, 'bk': 0, 'md': 0, 'or': 0}, index[0])
        self.weekly_cases_health = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0}, index=[0])
        self.weekly_cases_automaton = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])

        self.weekly_cases_symptomatic_age = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])
        self.weekly_cases_symptomatic_sex = pd.DataFrame({'m': 0, 'f': 0}, index[0])
        self.weekly_cases_symptomatic_ethnicity = pd.DataFrame({'we': 0, 'an': 0, 'bk': 0, 'md': 0, 'or': 0}, index[0])
        self.weekly_cases_symptomatic_health = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0}, index=[0])
        self.weekly_cases_symptomatic_automaton = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])

        self.weekly_cases_asymptomatic_age = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])
        self.weekly_cases_asymptomatic_sex = pd.DataFrame({'m': 0, 'f': 0}, index[0])
        self.weekly_cases_asymptomatic_ethnicity = pd.DataFrame({'we': 0, 'an': 0, 'bk': 0, 'md': 0, 'or': 0}, index[0])
        self.weekly_cases_asymptomatic_health = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0}, index=[0])
        self.weekly_cases_asymptomatic_automaton = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])

        self.weekly_self_isolating_age = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])
        self.weekly_self_isolating_sex = pd.DataFrame({'m': 0, 'f': 0}, index[0])
        self.weekly_self_isolating_ethnicity = pd.DataFrame({'we': 0, 'an': 0, 'bk': 0, 'md': 0, 'or': 0}, index[0])
        self.weekly_self_isolating_health = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0}, index=[0])
        self.weekly_self_isolating_automaton = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])

        self.weekly_recovered_age = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])
        self.weekly_recovered_sex = pd.DataFrame({'m': 0, 'f': 0}, index[0])
        self.weekly_recovered_ethnicity = pd.DataFrame({'we': 0, 'an': 0, 'bk': 0, 'md': 0, 'or': 0}, index[0])
        self.weekly_recovered_health = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0}, index=[0])
        self.weekly_recovered_automaton = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])

        self.weekly_deaths_age = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])
        self.weekly_deaths_sex = pd.DataFrame({'m': 0, 'f': 0}
        self.weekly_deaths_ethnicity = pd.DataFrame({'we': 0, 'an': 0, 'bk': 0, 'md': 0, 'or': 0}, index[0])
        self.weekly_deaths_health = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0}, index=[0])
        self.weekly_deaths_automaton = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])

        self.weekly_lockdowns_age = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, index[0])
        self.weekly_lockdowns_sex = pd.DataFrame({'m': 0, 'f': 0}, index[0])
        self.weekly_locdowns_ethnicity = pd.DataFrame({'we': 0, 'an': 0, 'bk': 0, 'md': 0, 'or': 0}, index[0])
        self.weekly_lockdowns_health = pd.DataFrame({0: 0, 1: 0, 2: 0, 3: 0, 4: 0}, index=[0])
        self.weekly_lockdowns_automaton = pd.DataFrame({0: False, 1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False}, index[0])

    def initialise(self, susceptible, cases_asymptomatic):
        for attribute in susceptible:
            self.weekly_susceptible_age[attribute[0]] += 1
            self.weekly_susceptible_sex[attribute[1]] += 1
            self.weekly_susceptible_ethnicity[attribute[2]] += 1
            self.weekly_susceptible_health[attribute[3]] += 1
            self.weekly_susceptible_automaton[attribute[4]] += 1

        for attribute in cases_asymptomatic:
            self.weekly_cases_asymptomatic_age[attribute[0]] += 1
            self.weekly_cases_asymptomatic_sex[attribute[1]] += 1
            self.weekly_cases_asymptomatic_ethnicity[attribute[2]] += 1
            self.weekly_cases_asymptomatic_health[attribute[3]] += 1
            self.weekly_cases_asymptomatic_automaton[attribute[4]] += 1

    def newWeek(self):
        for age in range(10):
            self.susceptible_age.iloc[:, age] += self.weekly_susceptible_age.iloc[:, age]
            self.weekly_susceptible_age.iloc[:, age] = 0
            self.exposed_age.iloc[:, age] += self.weekly_exposed_age.iloc[:, age]
            self.weekly_exposed_age.iloc[:, age] = 0
            self.cases_age.iloc[:, age] += self.weekly_cases_age.iloc[:, age]
            self.weekly_cases_age.iloc[:, age] = 0
            self.cases_symptomatic_age.iloc[:, age] += self.weekly_cases_symptomatic_age.iloc[:, age]
            self.weekly_cases_symptomatic_age.iloc[:, age] = 0
            self.cases_asymptomatic_age.iloc[:, age] += self.weekly_cases_asymptomatic_age.iloc[:, age]
            self.weekly_cases_asymptomatic_age.iloc[:, age] = 0
            self.self_isolating_age.iloc[:, age] += self.weekly_self_isolating_age.iloc[:, age]
            self.weekly_self_isolating_age.iloc[:, age] = 0
            self.recovered_age.iloc[:, age] += self.weekly_recovered_age.iloc[:, age]
            self.weekly_recoverd_age.iloc[:, age] = 0
            self.deaths_age.iloc[:, age] += self.weekly_deaths_age.iloc[:, age]
            self.weekly_deaths_age.iloc[:, age] = 0
            self.lockdowns_age.iloc[:, age] += self.weekly_lockdowns_age.iloc[:, age]
            # don't what to do here yet
            # self.weekly_lockdowns_age[age] = 0

        for sex in range(2):
            self.susceptible_sex.iloc[:, sex] += self.weekly_susceptible_sex.iloc[:, sex]
            self.weekly_susceptible_sex.iloc[:, sex] = 0
            self.exposed_sex.iloc[:, sex] += self.weekly_exposed_sex.iloc[:, sex]
            self.weekly_exposed_sex.iloc[:, sex] = 0
            self.cases_sex.iloc[:, sex] += self.weekly_cases_sex.iloc[:, sex]
            self.weekly_cases_sex.iloc[:, sex] = 0
            self.cases_symptomatic_sex.iloc[:, sex] += self.weekly_cases_symptomatic_sex.iloc[:, sex]
            self.weekly_cases_symptomatic_sex.iloc[:, sex] = 0
            self.cases_asymptomatic_sex.iloc[:, sex] += self.weekly_cases_asymptomatic_sex.iloc[:, sex]
            self.weekly_cases_asymptomatic_sex.iloc[:, sex] = 0
            self.self_isolating_sex.iloc[:, sex] += self.weekly_self_isolating_sex.iloc[:, sex]
            self.weekly_self_isolating_sex.iloc[:, sex] = 0
            self.recovered_sex.iloc[:, sex] += self.weekly_recovered_sex.iloc[:, sex]
            self.weekly_recovered_sex.iloc[:, sex] = 0
            self.deaths_sex.iloc[:, sex] += self.weekly_deaths_sex.iloc[:, sex]
            self.weekly_deaths_sex.iloc[:, sex] = 0
            self.lockdowns_sex.iloc[:, sex] += self.weekly_lockdowns_sex.iloc[:, sex]
            # don't know what to do here yet
            # self.weekly_lockdowns_sex[sex] = ?

        for ethnicity in range(5):
            self.susceptible_ethnicity.iloc[:, ethnicity] += self.weekly_susceptible_ethnicity.iloc[:, ethnicity]
            self.weekly_susceptible_ethnicity.iloc[:, ethnicity] = 0
            self.exposed_ethnicity.iloc[:, ethnicity] += self.weekly_exposed_ethnicity.iloc[:, ethnicity]
            self.weekly_exposed_ethnicity.iloc[:, ethnicity] = 0
            self.cases_ethnicity.iloc[:, ethnicity] += self.weekly_cases_ethnicity.iloc[:, ethnicity]
            self.weekly_cases_ethnicity.iloc[:, ethnicity] = 0
            self.cases_symptomatic_ethnicity.iloc[:, ethnicity] += self.weekly_cases_symptomatic_ethnicity.iloc[:, ethnicity]
            self.weekly_cases_symptomatic.iloc[:, ethnicity] = 0
            self.cases_asymptomatic_ethnicity.iloc[:, ethnicity] += self.weekly_cases_asymptomatic_ethnicity.iloc[:, ethnicity]
            self.weekly_cases_asymptomatic_ethnicity.iloc[:, ethnicity] = 0
            self.self_isolating_ethnictiy.iloc[:, ethnicity] += self.weekly_self_isolating_ethnicity.iloc[:, ethnicity]
            self.weekly_self_isolating_ethnicity.iloc[:, ethnicity] = 0
            self.recovered_ethnicity.iloc[:, ethnicity] += self.weekly_recovered_ethnicity.iloc[:, ethnicity]
            self.weekly_recovered_ethnicity.iloc[:, ethnicity] = 0
            self.deaths_ethnicity.iloc[:, ethnicity] += self.weekly_deaths_ethnicity.iloc[:, ethnicity]
            self.weekly_deaths_ethnicity.iloc[:, ethnicity] = 0
            self.lockdowns_ethnicity.iloc[:, ethnicity] += self.weekly_lockdowns_ethnicity.iloc[:, ethnicity]
            # don't know what to do here yet
            # self.weekly_lockdowns_ethnicity[ethnicity] = 0

        for health in range(5):
            self.susceptible_health.iloc[:, health] += self.weekly_susceptible_health.iloc[:, health]
            self.weekly_susceptible_health.iloc[:, health] = 0
            self.exposed_health.iloc[:, health] += self.weekly_exposed_health.iloc[:, health]
            self.weekly_exposed_health.iloc[:, health] = 0
            self.cases_health.iloc[:, health] += self.weekly_cases_health.iloc[:, health]
            self.weekly_cases_health.iloc[:, health] = 0
            self.cases_symptomatic_health.iloc[:, health] += self.weekly_cases_symptomatic_health.iloc[:, health]
            self.weekly_cases_symptomatic_health.iloc[:, health] = 0
            self.cases_asymptomatic_health.iloc[:, health] += self.weekly_cases_asymptomatic_health.iloc[:, health]
            self.weekly_cases_asymptomatic_health.iloc[:, health] = 0
            self.self_isolating_health.iloc[:, health] += self.weekly_self_isolating_health.iloc[:, health]
            self.weekly_self_isolating_health.iloc[:, health] = 0
            self.recovered_health.iloc[:, health] += self.weekly_recovered_health.iloc[:, health]
            self.weekly_recovered_health.iloc[:, health] = 0
            self.deaths_health.iloc[:, health] += self.weekly_deaths_health.iloc[:, health]
            self.weekly_deaths_health.iloc[:, health] = 0
            self.lockdowns_health.iloc[:, health] += self.weekly_health.iloc[:, health]
            # don't know what to here yet
            # self.weekly_lockdowns_health = ?

        for automaton in range(9):
            self.susceptible_automaton.iloc[:, automaton] += self.weekly_susceptible_automaton.iloc[:, automaton]
            self.weekly_susceptible_automaton.iloc[:, automaton] = 0
            self.exposed_automaton.iloc[:, automaton] += self.weekly_exposed_automaton.iloc[:, automaton]
            self.weekly_exposed_automaton.iloc[:, automaton] = 0
            self.cases_automaton.iloc[:, automaton] += self.weekly_cases_automaton.iloc[:, automaton]
            self.weekly_cases_automaton.iloc[:, automaton] = 0
            self.cases_symptomatic_automaton.iloc[:, automaton] += self.weekly_cases_symptomatic_automaton.iloc[:, automaton]
            self.weekly_cases_symptomatic_automaton.iloc[:, automaton] = 0
            self.cases_asymptomatic_automaton.iloc[:, automaton] += self.weekly_cases_automaton.iloc[:, automaton]
            self.weekly_cases_asymptomatic_automaton.iloc[:, automaton] = 0
            self.self_isolating_automaton.iloc[:, automaton] += self.weekly_self_isolating_automaton.iloc[:, automaton]
            self.weekly_self_isolating_automaton.iloc[:, automaton] = 0
            self.recovered_automaton.iloc[:, automaton] += self.weekly_recovered_automaton.iloc[:, automaton]
            self.weekly_recovered_automaton.iloc[:, automaton] = 0
            self.deaths_automaton.iloc[:, automaton] += self.weekly_deaths_automaton.iloc[:, automaton]
            self.weekly_deaths_automaton.iloc[:, automaton] = 0
            if self.weekly_lockdowns_automaton.iloc[:, automaton] == True:
                self.lockdowns_automaton.iloc[:, automaton] += 1
                # don't know what to do here yet
                # self.weekly_lockdowns_automaton[automaton] = ?

    def setSusceptible(self, attributes, automaton):
        for index in attributes:
            self.weekly_susceptible_age[index] += 1
            self.weekly_susceptible_sex[index] += 1
            self.weekly_susceptible_ethnicity[index] += 1
            self.weekly_susceptible_health[index] += 1
            self.weekly_susceptible_automaton[automaton] += 1

    def setExposed(self, attributes, automaton):
        for index in attributes:
            self.weekly_exposed_age[index] += 1
            self.weekly_exposed_sex[index] += 1
            self.weekly_exposed_ethnicity[index] += 1
            self.weekly_exposed_health[index] += 1
            self.weekly_exposed_automaton[automaton] += 1

    def setCaseSymptomatic(self, attributes, automaton):
        self.setCase(attributes, automaton)

        for index in attributes:
            self.weekly_cases_symptomatic_age[index] += 1
            self.weekly_cases_symptomatic_sex[index] += 1
            self.weekly_cases_symptomatic_ethnicity[index] += 1
            self.weekly_cases_symptomatic_health[index] += 1
            self.weekly_cases_symptomatic_automaton[automaton] += 1

    def setCaseAsymptomatic(self, attributes, automaton):
        self.setCase(attributes, automaton)

        for index in attributes:
            self.weekly_cases_asymptomatic_age[index] += 1
            self.weekly_cases_asymptomatic_sex[index] += 1
            self.weekly_cases_asymptomatic_ethnicity[index] += 1
            self.weekly_cases_asymptomatic_health[index] += 1
            self.weekly_cases_asymptomatic_automaton[automaton] += 1
            
    @abstractmethod
    def setCase(self, attributes, automaton):
        for index in attributes:
            self.weekly_cases_age[index] += 1
            self.weekly_cases_sex[index] += 1
            self.weekly_cases_ethnicity[index] += 1
            self.weekly_cases_health[index] += 1
            self.weekly_cases_automaton[automaton] += 1

    def setSelfIsolation(self):
        for index in attributes:
            self.weekly_self_isolating_age[index] += 1
            self.weekly_self_isolating_sex[index] += 1
            self.weekly_self_isolating_ethnicity[index] += 1
            self.weekly_self_isolating_health[index] += 1
            self.weekly_self_isolating_automaton[automaton] += 1

    def setRecovery(self, automaton):
        for index in attributes:
            self.weekly_recovered_age[index] += 1
            self.weekly_recovered_sex[index] += 1
            self.weekly_recovered_ethnicity[index] += 1
            self.weekly_recovered_health[index] += 1
            self.weekly_recovered_automaton[automaton] += 1

    def setDeath(self):
        for index in attributes:
            self.weekly_deaths_age[index] += 1
            self.weekly_deaths_sex[index] += 1
            self.weekly_deaths_ethnicity[index] += 1
            self.weekly_deaths_health[index] += 1
            self.weekly_deaths_automaton[automaton] += 1

    def setLockdowns(self, lockdowns):
        pass
