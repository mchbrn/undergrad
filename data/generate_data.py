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

def ethnicity(random3):
    # White
    if (random3 <= 0.9828):
        data = "we,"
        return data
    # Asian
    elif (random3 <= 0.9934):
        data = "an,"
        return data
    # Asian
    elif (random3 <= 0.9954):
        data = "bk,"
        return data
    # Black
    elif (random3 <= 0.9987):
        data = "md,"
        return data
    # Other
    elif (random3 <= 1.0):
        data = "or,"
        return data

def health(random4):
    # Very good health
    if (random4 <= 0.4772):
        data = "4,"
        return data
    # Good health
    elif (random4 <= 0.7951):
        data = "3,"
        return data
    # Fair health
    elif (random4 <= 0.9436):
        data = "2,"
        return data
    # Bad health
    elif (random4 <= 0.9881):
        data = "1,"
        return data
    # Very bad health
    elif (random4 <= 1.0):
        data = "0,"
        return data

def state(random5):
    if (random5 <= 0.01):
        data = "I,"
        return data
    elif (random5 <= 1.00):
        data = "S,"
        return data

def town(random6):
    # belfast
    if (random6 <= 0.3383):
        data = "0"
        return data
    # derry
    elif (random6 <= 0.4220):
        data = "1"
        return data
    # newtownabbey
    elif (random6 <= 0.4881):
        data = "2"
        return data
    # cragiavon
    elif (random6 <= 0.5528):
        data = "3"
        return data
    # bangor
    elif (random6 <= 0.6142):
        data = "4"
        return data
    # lisburn
    elif (random6 <= 0.6599):
        data = "5"
        return data
    # ballymena
    elif (random6 <= 0.6897):
        data = "6"
        return data
    # newtownards
    elif (random6 <= 0.7179):
        data = "7"
        return data
    # carrickfergus
    elif (random6 <= 0.7461):
        data = "8"
        return data
    # newry
    elif (random6 <= 0.7733):
        data = "9"
        return data
    # coleraine
    elif (random6 <= 0.7980):
        data = "10"
        return data
    # antrim
    elif (random6 <= 0.8216):
        data = "11"
        return data
    # omagh
    elif (random6 <= 0.8414):
        data = "12"
        return data
    # larne
    elif (random6 <= 0.8602):
        data = "13"
        return data
    # banbridge
    elif (random6 <= 0.8770):
        data = "14"
        return data
    # armagh
    elif (random6 <= 0.8919):
        data = "15"
        return data
    # dungannon
    elif (random6 <= 0.9063):
        data = "16"
        return data
    # enniskillen
    elif (random6 <= 0.9202):
        data = "17"
        return data
    # strabane
    elif (random6 <= 0.9335):
        data = "18"
        return data
    # limavady
    elif (random6 <= 0.9456):
        data = "19"
        return data
    # cookstown
    elif (random6 <= 0.9573):
        data = "20"
        return data
    # holywood
    elif (random6 <= 0.9686):
        data = "21"
        return data
    # downpatrick
    elif (random6 <= 0.9795):
        data = "22"
        return data
    # ballymoney
    elif (random6 <= 0.9900):
        data = "23"
        return data
    # ballyclare
    elif (random6 <= 1.0000):
        data = "24"
        return data

with open('population.csv', 'w') as f:
    for i in range(75701):
        data = ""

        seed()
        random1 = random()

        my_age = age(random1)

        seed()
        random2 = random()

        my_sex = sex(random2)

        seed()
        random3 = random()

        my_ethnicity = ethnicity(random3)

        seed()
        random4 = random()

        my_health = health(random4)

        seed()
        random5 = random()

        my_state = state(random5)

        seed()
        random6 = random()

        my_town = town(random6)

        data += my_age + my_sex + my_ethnicity + my_health + my_state + my_town + "\n"
        f.write(data)
