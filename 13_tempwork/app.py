# Ivan Gontchar
# Flying Fire Belugas: Ivan, Tanzeem, Jason
# SoftDev
# K13 - Template for Success
# Sep 2024
# time spent: 1 hour
'''DISCO:

QCC:'''

from flask import Flask, render_template
import random
app = Flask(__name__)

def maker():
    returner = "The industry you got is "
    with open("data/occupations.csv", "r") as file:
        f = file.read()
    arr = f.split("\n")
    #print(arr)
    dict = {}
    total = 0
    for i in range(1, len(arr[1:len(arr)-1])):
        if arr[i][0] == '\"':
            x = arr[i].split("\",")
            temp = x[1].split(",")
            #print(temp)
            x[1] = temp[0]
            x.append(temp[1])
            #print(x)
            #print(arr[i].split("\","))
            #total += int(x[1])
            y = [x[0][1:], float(x[1]), x[2]]
            #print(y)
            total += y[1]
            dict[total] = y
        else:
            x = arr[i].split(",")
            #print(x)
            y = [x[0], float(x[1]), x[2]]
            total += y[1]
            dict[total] = y
    #pprint.pp(dict)
    x = random.random() * 99.8;
    choice = [];
    temp = list(dict.keys())
    for i in temp:
        if(i > x):
            choice = dict.get(i)
            break
    #print(x)
    #print(choice)
    returner += choice[0]
    returner += ", that takes up " + str(choice[1]) + "% of the job market."
    #print("The industry you got is " + choice[0] + ", that takes up", choice[1], "% of the job market.")
    return returner

@app.route("/")
def hello_world():
    return maker()

with open("data/occupations.csv", "r") as file:
    f = file.read()
    arr = f.split("\n")
    arr = arr[:-1]
    #print(arr)
    #print(arr)
    dict = {}
    total = 0
    for i in range(len(arr)):
        #print(arr)
        #print(arr[i])
        if arr[i][0] == '\"':
            x = arr[i].split("\",")
            temp = x[1].split(",")
            #print(temp)
            x[1] = temp[0]
            x.append(temp[1])
            #print(x)
            #print(arr[i].split("\","))
            #total += int(x[1])
            arr[i] = [x[0][1:], x[1], x[2]]
            #print(y)
        else:
            x = arr[i].split(",")
            #print(x)
            arr[i] = [x[0], x[1], x[2]]
            #print(arr[i])


@app.route("/wdywtbwygp")
def test_tmplt():
    #print(arr)
    return render_template( 'tablified.html',
        title="Random Occupation",
        header="Choosing Occupation from Table",
        TNPG="Flying Fire Belugas: Ivan, Tanzeem, Jason",
        randChoice=maker(),
        topper=arr[0],
        file=arr[1:])


if __name__ == "__main__":
    app.debug = True
    app.run()
