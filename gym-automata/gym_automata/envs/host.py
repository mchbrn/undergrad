from random import random
from random import seed

class Host:
    def __init__(self, number, age, sex, ethnicity, health, state, home):
        self.number = number
        self.age = age
        self.sex = sex
        self.ethnicity = ethnicity
        self.health = health
        self.state = state
        self.symptomatic = None
        self.home = home
        # how many days since last state change
        self.counter = 0
        self.threshold = setThreshold()

    def getAttributes(self):
        attributes = [self.age, self.sex, self.ethnicity, self.health, self.home]
        return attributes

    def getState(self):
        return self.state

    def setState(self):
        self.state += 1
        self.counter = 0

    def setThreshold(self):
        threshold = 0.99

        # 18 - 19
        if self.age == 0:
            threshold -= 0.00
        # 20 - 24
        elif self.age == 1:
            threshold -= 0.05
        # 25 - 29
        elif self.age == 2:
            threshold -= 0.10
        # 30 - 44
        elif self.age == 3:
            threshold -= 0.15
        # 45 - 59
        elif self.age == 4:
            threshold -= 0.20
        # 60 - 64
        elif self.age == 5:
            threshold -= 0.25
        # 65 - 74
        elif self.age == 6:
            threshold -= 0.30
        # 75 - 84
        elif self.age == 7:
            threshold -= 0.35
        # 85 - 89
        elif self.age == 8:
            threshold -= 0.40
        # 90 - ∞
        elif self.age == 9:
            threshold -= 0.45

        # female
        if self.sex == 'f':
            threshold -= 0.00
        # male
        elif self.sex == 'm':
            threshold -= 0.04

        # white
        if self.ethnicity == 'we':
            threshold -= 0.00
        # asian
        elif self.ethnictiy == 'an':
            threshold -= 0.01
        # black
        elif self.ethnictiy == 'bk':
            threshold -= 0.04
        # mixed
        elif self.ethnictiy == 'md':
            threshold -= 0.02
        # other
        elif self.ethnictiy == 'or':
            threshold -= 0.03

        # very good health
        if self.health == 0:
            threshold -= 0.0000
        # good health
        elif self.health == 1:
            threshold -= 0.1125
        # fair health
        elif self.health == 2:
            threshold -= 0.2250
        # bad health
        elif self.health == 3:
            threshold -= 0.3375
        # very bad health
        elif self.health == 4:
            threshold -= 0.4500

        return threshold
        
    def setCounter(self):
        self.counter += 1

    def getHome(self):
        return self.home

    def infect(self):
        seed()
        chance_of_infection = random()

        if chance_of_infection < 0.5:
            seed()
            self.setState()
        else:
            return None

        infection = [self.state, self.infectious]
        return infection
