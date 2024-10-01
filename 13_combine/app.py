# Ivan Gontchar
# Flying Fire Belugas: Ivan, Tanzeem, Jason
# SoftDev
# K13 - Template for Success
# Sep 2024
# time spent:
'''DISCO:

QCC:'''

from flask import Flask, render_template
import numbercruncher
app = Flask(__name__)

@app.route("/")
def hello_world():
    return numbercruncher.maker()

with open("occupations.csv", "r") as file:
    f = file.read()
arr = f.split("\n")
for i in range(len(arr) -1 ):
    if arr[i][0] == '\"':
        arr[i] = arr[i].split("\",")
        #print(arr[i].split("\","))
        #total += int(x[1])
        #y = [x[0][1:], float(x[1])]
        #total += y[1]
        #dict[total] = y
    else:
        arr[i] = arr[i].split(",")
        #print(x)
        #y = [x[0], float(x[1])]
        #total += y[1]
        #dict[total] = y

@app.route("/wdywtbwygp")
def test_tmplt():
    print(arr)
    return render_template( 'occupations.html',
        title="Random Occupation",
        header="Choosing Occupation from Table",
        TNPG="Flying Fire Belugas: Ivan, Tanzeem, Jason",
        file=arr)


if __name__ == "__main__":
    app.debug = False
    app.run()
