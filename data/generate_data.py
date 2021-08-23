from random import random
from random import seed
from random import randrange

age = []
sex = []
health = []
state = []
district = []

for i in range(95):
    age.append(0)

for i in range(175):
    age.append(1)

for i in range(173):
    age.append(2)

for i in range(434):
    age.append(3)

for i in range(407):
    age.append(4)

for i in range(142):
    age.append(5)

for i in range(214):
    age.append(6)

for i in range(134):
    age.append(7)

for i in range(65):
    age.append(8)

for i in range(54):
    age.append(9)

for i in range(928):
    sex.append("m")

for i in range(965):
    sex.append("f")

for i in range(903):
    health.append(0)

for i in range(602):
    health.append(1)

for i in range(281):
    health.append(2)

for i in range(84):
    health.append(3)

for i in range(23):
    health.append(4)

for i in range(1874):
    state.append(0)

for i in range(19):
    state.append(2)

for i in range(344):
    district.append(0)

for i in range(216):
    district.append(1)

for i in range(181):
    district.append(2)

for i in range(162):
    district.append(3)

for i in range(151):
    district.append(4)

for i in range(149):
    district.append(5)

for i in range(146):
    district.append(6)

for i in range(145):
    district.append(7)

for i in range(144):
    district.append(8)

for i in range(139):
    district.append(9)

for i in range(117):
    district.append(10)

with open("population.csv", "w") as f:
    f.write("number,age,sex,health,state,district\n")
    for i in range(1893):
        len_age = len(age)
        len_sex = len(sex)
        len_health = len(health)
        len_state = len(health)
        len_district = len(district)

        seed()
        random_age = randrange(0, len_age, 1)
        host_age = age[random_age]
        age.pop(random_age)

        seed()
        random_sex = randrange(0, len_sex, 1)
        host_sex = sex[random_sex]
        sex.pop(random_sex)

        seed()
        random_health = randrange(0, len_health, 1)
        host_health = health[random_health]
        health.pop(random_health)

        seed()
        random_state = randrange(0, len_state, 1)
        host_state = state[random_state]
        state.pop(random_state)

        seed()
        random_district = randrange(0, len_district, 1)
        host_district = district[random_district]
        district.pop(random_district)

        data = str(i) + "," + str(host_age) + "," + str(host_sex) + "," + str(host_health) + "," + str(host_state) + "," + str(host_district) + "\n"

        f.write(data)
