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
        if self.state = 2:
            # none, asymptomatic, presymptomatic and symptomatic
            self.symptoms = "asymptomatic"
            self.infectious = True
        else:
            self.symptoms = None
            self.infectious = False
        self.home = home
        # how many days since last state change
        self.counter = 0 

    def getState(self):
        return self.state

    def setState(self):
        self.state += 1
        self.counter = 0

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

        seed()
        chance_of_symptoms = random()

        if chance_of_symptoms >= 0.8:
            self.symptoms = "presymptomatic"
        else:
            self.symptoms = "asymptomatic"

        infection = [self.state, self.symptoms]
        return infection
