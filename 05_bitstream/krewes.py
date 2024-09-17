# Ivan Gontchar
# Belugas
# SoftDev
# K05 -- Python Random Selection & Dictionaries
# 2024-9-17
# Time Spent:
import random

file = open("krewes.txt", "r")
info = file.read().strip()
#print(info)
perPerson = info.split("@@@")
#print(perPerson)

per4 = []
per5 = []

for i in perPerson:
    x = i.split("$$$")
    #print(x)
    if x[0] == '4':
        per4.append(x[1:])
    else:
        per5.append(x[1:])

#print(per4)
#print(per5)

krewes = {
    4: per4,
    5: per5
}

#print(krewes)

periodChoice = random.choice(list(krewes.keys()))
#print(periodChoice)
personChoice = random.choice(list(krewes[periodChoice]))
#print(personChoice)

print(personChoice[0] + " of period " + str(periodChoice) + " and their friend " + personChoice[1])
