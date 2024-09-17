# Ivan Gontchar
# Belugas
# SoftDev
# K05 -- Python Random Selection & Dictionaries
# 2024-9-17
# Time Spent:
import random

file = open("krewes.txt", "r")
info = file.read()
print(info)
for i in range(len(info)):
    

krewes = {
    4: [],
    5: []
}



value = random.choice(list(krewes.values()))
print(random.choice(value))
