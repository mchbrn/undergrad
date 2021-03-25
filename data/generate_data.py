from random import seed
from random import random

def age(random1):
    # 0 - 15
    if (random1 <= 0.167):
        data = "0,"
        return data
    # 16 - 44
    elif (random1 <= 0.621):
        data = "1,"
        return data
    # 45 - 64
    elif (random1 <= 0.859):
        data = "2,"
        return data
    # 65 - ∞
    elif (random1 <= 1.0):
        data = "3,"
        return data

def sex(random2):
    # Male
    if (random2 <= 0.494):
        data = "m,"
        return data
    # Female
    elif (random2 <= 1.0):
        data = "f,"
        return data

def ethnicity(random3):
    # White
    if (random3 <= 0.889):
        data = "We,"
        return data
    # Mixed
    elif (random3 <= 0.914):
        data = "Md,"
        return data
    # Asian
    elif (random3 <= 0.956):
        data = "An,"
        return data
    # Black
    elif (random3 <= 0.982):
        data = "Bk,"
        return data
    # Arab
    elif (random3 <= 0.994):
        data = "Ab,"
        return data
    # Other
    elif (random3 <= 1.0):
        data = "Or,"
        return data

def employment(random4, sex):
    if (sex == "m,"):
        # Economically active
        if (random4 <= 0.665):
            data = "1,"
            return data
        # Economically inactive
        elif (random4 <= 1.0):
            data = "0,"
            return data
    elif (sex == "f,"):
        # Economically active
        if (random4 <= 0.604):
            data = "1,"
            return data
        # Economically inactive
        elif (random4 <= 1.0):
            data = "0,"
            return data

def health(random5):
    # Very good health
    if (random5 <= 0.467):
        data = "4,"
        return data
    # Good health
    elif (random5 <= 0.772):
        data = "3,"
        return data
    # Fair health
    elif (random5 <= 0.912):
        data = "2,"
        return data
    # Bad health
    elif (random5 <= 0.979):
        data = "1,"
        return data
    # Very bad health
    elif (random5 <= 1.0):
        data = "0,"
        return data

def ward(random6):
    if (random6 <= 0.0318):
        data = "1"
        return data
    elif (random6 <= 0.0629):
        data = "2"
        return data
    elif (random6 <= 0.0951):
        data = "3"
        return data
    elif (random6 <= 0.1387):
        data = "4"
        return data
    elif (random6 <= 0.1685):
        data = "5"
        return data
    elif (random6 <= 0.1985):
        data = "6"
        return data
    elif (random6 <= 0.2312):
        data = "7"
        return data
    elif (random6 <= 0.2613):
        data = "8"
        return data
    elif (random6 <= 0.2924):
        data = "9"
        return data
    elif (random6 <= 0.3236):
        data = "10"
        return data
    elif (random6 <= 0.3553):
        data = "11"
        return data
    elif (random6 <= 0.3913):
        data = "12"
        return data
    elif (random6 <= 0.4259):
        data = "13"
        return data
    elif (random6 <= 0.4589):
        data = "14"
        return data
    elif (random6 <= 0.4935):
        data = "15"
        return data
    elif (random6 <= 0.5220):
        data = "16"
        return data
    elif (random6 <= 0.5516):
        data = "17"
        return data
    elif (random6 <= 0.5839):
        data = "18"
        return data
    elif (random6 <= 0.6192):
        data = "19"
        return data
    elif (random6 <= 0.6557):
        data = "20"
        return data
    elif (random6 <= 0.6924):
        data = "21"
        return data
    elif (random6 <= 0.7319):
        data = "22"
        return data
    elif (random6 <= 0.7754):
        data = "23"
        return data
    elif (random6 <= 0.8033):
        data = "24"
        return data
    elif (random6 <= 0.8387):
        data = "25"
        return data
    elif (random6 <= 0.8740):
        data = "26"
        return data
    elif (random6 <= 0.9057):
        data = "27"
        return data
    elif (random6 <= 0.9365):
        data = "28"
        return data
    elif (random6 <= 0.9642):
        data = "29"
        return data
    elif (random6 <= 1.0000):
        data = "30"
        return data

with open('population.csv', 'w') as f:
    for i in range(46642):
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

        my_employment = employment(random4, my_sex)

        seed()
        random5 = random()

        my_health = health(random5)

        seed()
        random6 = random()

        my_ward = ward(random6)

        data += my_age + my_sex + my_ethnicity + my_employment + my_health + my_ward + "\n"
        f.write(data)