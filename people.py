#digital community full of profiles
#how to create a complete virtual community?fake profiles, no physical existence
import random
import math
from time import datetime

class People(object):

    def __init__(self, first_name, last_name, gender, age, profession, income, race):
        self.first_name=first_name
        self.last_name=last_name
        self.gender=gender
        self.age=age
        self.profession=profession
        self.income=income
        self.race=race

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def age(self):
        return random.randint(1, 130)

    def gender(self):
        return random.choice(["male", "female"])

class real_people(People):

    def __init__(self, first_name, last_name, gender, age, profession, residential_address):
        super(real_people, self).__init__(first_name, last_name, gender, income)
        self.residential_address=residential_address
       

class fake_people(People):
    
    def __init__(self, first_name, last_name, gender, age, profession, manufacture_date):
        super(fake_people, self).__init__(first_name, last_name, gender, age, profession)
        self.manufacture_date=manufacture_date


p_1=People("Julia", "Roberts", female, 49)
p_2=People("Sandra", "Evans", female, 54)


print People.fullname(p_1)

