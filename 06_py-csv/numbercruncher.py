# Icebroken (Tanzeem Hasan and Ivan Gontchar)
# SoftDev
# K06:: "The More You Know About Your Data..."
# 2024 - 09 - 19
# Time spent:

'''
Disco:
QCC:
HOW THIS SCRIPT WORKS
'''

import random

with open("occupations.csv", "r") as file:
    f = file.read()
arr = f.split("\n")
#print(arr)
dict = {}
total = 0
for i in range(len(arr[1:len(arr)-1])):
    if arr[i][0] == '\"':
        x = arr[i].split("\",")
        #print(arr[i].split("\","))
        #total += int(x[1])
        y = [x[0][1:], float(x[1])]
        total += y[1]
        dict[total] = y
    else:
        x = arr[i].split(",")
print(dict)
