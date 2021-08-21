from host import Host
from random import seed
from random import random

def age(random1):
    # 18 - 19
    if (random1 <= 0.05149):
        data = 0
        return data
    # 20 - 24
    elif (random1 <= 0.14488):
        data = 1
        return data
    # 25 - 29
    elif (random1 <= 0.23717):
        data = 2
        return data
    # 30 - 44
    elif (random1 <= 0.46746):
        data = 3
        return data
    # 45 - 59
    elif (random1 <= 0.68335):
        data = 4
        return data
    # 60 - 64
    elif (random1 <= 0.75924):
        data = 5
        return data
    # 65 - 74
    elif (random1 <= 0.87343):
        data = 6
        return data
    # 75 - 84
    elif (random1 <= 0.94512):
        data = 7
        return data
    # 85 - 89
    elif (random1 <= 0.98061):
        data = 8
        return data
    # 90 - ∞
    elif (random1 <= 1.0):
        data = 9
        return data

def sex(random2):
    # Male
    if (random2 <= 0.49):
        data = "m"
        return data
    # Female
    elif (random2 <= 1.0):
        data = "f"
        return data

def health(random3):
    # very good health
    if (random3 <= 0.4772):
        data = 0
        return data
    # good health
    elif (random3 <= 0.7951):
        data = 1
        return data
    # fair health
    elif (random3 <= 0.9436):
        data = 2
        return data
    # bad health
    elif (random3 <= 0.9881):
        data = 3
        return data
    # very bad health
    elif (random3 <= 1.0):
        data = 4
        return data

def district(random5):
    # antrim and newtownabbey
    if (random5 <= 0.0760):
        data = 0
        return data
    # ards and north down
    elif (random5 <= 0.1616):
        data = 1
        return data
    # armagh city, banbridge and craigavon
    elif (random5 <= 0.2756):
        data = 2
        return data
    # belfast
    elif (random5 <= 0.4572):
        data = 3
        return data
    # causeway coast and glens
    elif (random5 <= 0.5338):
        data = 4
        return data
    # derry city and strabane
    elif (random5 <= 0.6135):
        data = 5
        return data
    # fermanagh and omagh
    elif (random5 <= 0.6753):
        data = 6
        return data
    # lisburn and castlereagh
    elif (random5 <= 0.7524):
        data = 7
        return data
    # mid and east antrim
    elif (random5 <= 0.8258):
        data = 8
        return data
    # mid ulster
    elif (random5 <= 0.9044):
        data = 9
        return data
    # newry, mourne and down
    elif (random5 <= 1.0000):
        data = 10
        return data

def generate_hosts(number_of_hosts, host_number):
    hosts = []

    for i in range(number_of_hosts):
        seed()
        random1 = random()

        host_age = age(random1)

        seed()
        random2 = random()

        host_sex = sex(random2)

        seed()
        random3 = random()

        host_health = health(random3)

        seed()
        random5 = random()

        host_district = district(random5)

        host = Host(host_number, host_age, host_sex, host_health, 2, host_district)

        hosts.append(host)
        host_number += 1

    return hosts
