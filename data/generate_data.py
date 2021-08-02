from random import seed
from random import random

def age(random1):
    # 18 - 19
    if (random1 <= 0.05149):
        data = "0,"
        return data
    # 20 - 24
    elif (random1 <= 0.14488):
        data = "1,"
        return data
    # 25 - 29
    elif (random1 <= 0.23717):
        data = "2,"
        return data
    # 30 - 44
    elif (random1 <= 0.46746):
        data = "3,"
        return data
    # 45 - 59
    elif (random1 <= 0.68335):
        data = "4,"
        return data
    # 60 - 64
    elif (random1 <= 0.75924):
        data = "5,"
        return data
    # 65 - 74
    elif (random1 <= 0.87343):
        data = "6,"
        return data
    # 75 - 84
    elif (random1 <= 0.94512):
        data = "7,"
        return data
    # 85 - 89
    elif (random1 <= 0.98061):
        data = "8,"
        return data
    # 90 - ∞
    elif (random1 <= 1.0):
        data = "9,"
        return data

def sex(random2):
    # Male
    if (random2 <= 0.49):
        data = "m,"
        return data
    # Female
    elif (random2 <= 1.0):
        data = "f,"
        return data

def health(random3):
    # very good health
    if (random3 <= 0.4772):
        data = "0,"
        return data
    # good health
    elif (random3 <= 0.7951):
        data = "1,"
        return data
    # fair health
    elif (random3 <= 0.9436):
        data = "2,"
        return data
    # bad health
    elif (random3 <= 0.9881):
        data = "3,"
        return data
    # very bad health
    elif (random3 <= 1.0):
        data = "4,"
        return data

def stateAndTown(random5, random6):
    # antrim and newtownabbey
    if (random5 <= 0.0760):
        # infectious
        if (random6 <= 0.03):
            data = "2,0"
            return data
        # susceptible
        elif (random6 <= 1.00):
            data = "0,0"
            return data
    # ards and north down
    elif (random5 <= 0.1616):
        # infectious
        if (random6 <= 0.01):
            data = "2,1"
            return data
        # susceptible
        elif (random6 <= 1.00):
            data = "0,1"
            return data
    # armagh city, banbridge and craigavon
    elif (random5 <= 0.2756):
        # infectious
        if (random6 <= 0.01):
            data = "2,2"
            return data
        # susceptible
        elif (random6 <= 1.00):
            data = "0,2"
            return data
    # belfast
    elif (random5 <= 0.4572):
        # infectious
        if (random6 <= 0.01):
            data = "2,3"
            return data
        # susceptible
        elif (random6 <= 1.00):
            data = "0,3"
            return data
    # causeway coast and glens
    elif (random5 <= 0.5338):
        # infectious
        if (random6 <= 0.01):
            data = "2,4"
            return data
        # susceptible
        elif (random6 <= 1.00):
            data = "0,4"
            return data
    # derry city and strabane
    elif (random5 <= 0.6135):
        # infectious
        if (random6 <= 0.01):
            data = "2,5"
            return data
        # susceptible
        elif (random6 <= 1.00):
            data = "0,5"
            return data
    # fermanagh and omagh
    elif (random5 <= 0.6753):
        # infectious
        if (random6 <= 0.01):
            data = "2,6"
            return data
        # susceptible
        elif (random6 <= 1.00):
            data = "0,6"
            return data
    # lisburn and castlereagh
    elif (random5 <= 0.7524):
        # infectious
        if (random6 <= 0.01):
            data = "2,7"
            return data
        # susceptible
        elif (random6 <= 1.00):
            data = "0,7"
            return data
    # mid and east antrim
    elif (random5 <= 0.8258):
        # infectious
        if (random6 <= 0.01):
            data = "2,8"
            return data
        # susceptible
        elif (random6 <= 1.00):
            data = "0,8"
            return data
    # mid ulster
    elif (random5 <= 0.9044):
        # infectious
        if (random6 <= 0.01):
            data = "2,9"
            return data
        # susceptible
        elif (random6 <= 1.00):
            data = "0,9"
            return data
    # newry, mourne and down
    elif (random5 <= 1.0000):
        # infectious
        if (random6 <= 0.01):
            data = "2,10"
            return data
        # susceptible
        elif (random6 <= 1.00):
            data = "0,10"
            return data

with open('population.csv', 'w') as f:
    for i in range(1894):
        data = str(i) + ","

        seed()
        random1 = random()

        my_age = age(random1)

        seed()
        random2 = random()

        my_sex = sex(random2)

        seed()
        random3 = random()

        my_health = health(random3)

        seed()
        random5 = random()
        seed()
        random6 = random()

        my_state_and_town = stateAndTown(random5, random6)

        data += my_age + my_sex + my_health + my_state_and_town + "\n"
        f.write(data)
