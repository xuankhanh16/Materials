
people = []
with open('people.txt', r) as file:
    for line in file:
        name, dob, identity = line.strip().split(',')
        

