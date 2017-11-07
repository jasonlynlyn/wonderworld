#generate 20 profiles randomly age 18-45

import random

first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria']
last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']
sex= ["male", "female"]




for n in range(1, 21): #generating 20 profiles
    first = random.choice(first_names)
    last = random.choice(last_names)
    name = first + ' ' + last
    age = random.randint(18, 45)
    gender = random.choice(sex)
    print str(n) + ' ' + '{}, {}, {}'.format(name, gender, age) 