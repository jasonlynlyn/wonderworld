#digital community full of profiles
#how to create a complete virtual community?fake profiles, no physical existence
import random
import math
from time import datetime

#creating random birthdays
class birthdays(math, random):

    def __init__(self, day, month, year):
        self.day=day
        self.month=month
        self.year=year

    def main(self): #random birthday combination
        pass


#creating random residential address
#creating random






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


def Profile(): #creating objects
    real_profile = real_people()
    fake_profile = fake_people()
    real_profile.residential_address = "rejdkfaljfa"
    fake_profile.manufacture_date = "slkjfljdflkds"


# p_1=People("Julia", "Roberts", female, 49)
# p_2=People("Sandra", "Evans", female, 54)


# print People.fullname(p_1)

if __name__=="__main__":
    Profile()
