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
        self.symptomatic = False
        self.self_isolating = False
        self.home = home
        # how many days since last state change
        self.counter = 0
        self.threshold = self.setThreshold()

    def getAttributes(self):
        attributes = [self.age, self.sex, self.ethnicity, self.health]
        return attributes

    def setState(self):
        if self.state == 3:
            self.state = 0
        else:
            self.state += 1

        self.counter = 0

    def setThreshold(self):
        threshold = 0.99

        # 18 - 19
        if self.age == 0:
            threshold -= 0.01
        # 20 - 24
        elif self.age == 1:
            threshold -= 0.02
        # 25 - 29
        elif self.age == 2:
            threshold -= 0.03
        # 30 - 44
        elif self.age == 3:
            threshold -= 0.04
        # 45 - 59
        elif self.age == 4:
            threshold -= 0.06
        # 60 - 64
        elif self.age == 5:
            threshold -= 0.09
        # 65 - 74
        elif self.age == 6:
            threshold -= 0.14
        # 75 - 84
        elif self.age == 7:
            threshold -= 0.21
        # 85 - 89
        elif self.age == 8:
            threshold -= 0.30
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
        elif self.ethnicity == 'an':
            threshold -= 0.01
        # black
        elif self.ethnicity == 'bk':
            threshold -= 0.04
        # mixed
        elif self.ethnicity == 'md':
            threshold -= 0.02
        # other
        elif self.ethnicity == 'or':
            threshold -= 0.03

        # very good health
        if self.health == 0:
            threshold -= 0.00
        # good health
        elif self.health == 1:
            threshold -= 0.02
        # fair health
        elif self.health == 2:
            threshold -= 0.06
        # bad health
        elif self.health == 3:
            threshold -= 0.17
        # very bad health
        elif self.health == 4:
            threshold -= 0.45

        return threshold
        
    def setCounter(self):
        self.counter += 1

    def infect(self):
        seed()
        chance_of_infection = random()

        if chance_of_infection < 0.5:
            seed()
            self.setState()
            attributes = self.getAttributes()
            return attributes
        else:
            return None
