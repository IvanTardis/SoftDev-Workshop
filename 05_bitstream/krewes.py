# Ivan Gontchar
# Belugas
# SoftDev
# K05 -- Python Random Selection & Dictionaries
# 2024-9-17
# Time Spent: 50 minutes = 0.83 hours

import random

file = open("krewes.txt", "r") # This opens up the txt file as a file object into variable file

info = file.read().strip() # .read() is a method for file objects, which turns it into a string.
                           # .strip() is simply to clean up the newline character at the end, or
                           # any messiness on the edges

perPerson = info.split("@@@") # this splits the string anywhere where there is a "@@@", into a list
                              # with the everything that was split as a string in the list
                              # this results in a list where each element is:
                              # 'pd$$$devo$$$ducky'

per4 = []
per5 = []

for i in perPerson:
    x = i.split("$$$") # like the previous split, this breaks the string at the "$$$" seperator into
                       # a list. since the loop is going through each string in the previous list
                       # the result, x, is a list with ['pd', 'devo', 'ducky']
    #print(x)
    if x[0] == '4': # which period's list do we add to
        per4.append(x[1:]) # this adds the devo and ducky name only
    else:
        per5.append(x[1:]) # same here


# making our dictionary with all our devos and duckies
krewes = {
    4: per4,
    5: per5
}


periodChoice = random.choice(list(krewes.keys())) # here we get a list of all the keys in the
                                                  # dictionary, which are only 4 and 5, and
                                                  # then we pick a random one of them

personChoice = random.choice(list(krewes[periodChoice])) # here we get a list of all the values
                                                         # of the key that we just randomly picked
                                                         # (all the devos and duckies of a given pd)
                                                         # and choose a random one of those


#printing our random choice asthetically
print(personChoice[0] + " of period " + str(periodChoice) + " and their friend " + personChoice[1])
