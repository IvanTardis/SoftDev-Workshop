# Dualbeans (Ivan, Michelle)
# SoftDev
# K23: A RESTful Journey Skyward
# 2024-11-20
# time spent: 30 minutes

from flask import Flask, render_template, request, session, redirect, url_for
import urllib.request
import pprint
import json

app = Flask(__name__)    #create Flask object

# makin' a supa-secret key
app.secret_key = "1234";

file = open("key_nasa.txt")
myKey = file.readline()

myLink = "https://api.nasa.gov/planetary/apod?api_key=" + myKey
# print(myLink)
myURL = urllib.request.urlopen(myLink)
# print(myURL.geturl())
# print(myURL.info())

s = myURL.read()
# print(s)
dict = json.loads(s)
# pprint.pp(dict)

imgURL = dict['url']
description = dict['title']
explanation = dict['explanation']
# print(imgURL)

@app.route(("/") , methods=['GET', 'POST'])
def home():
    return render_template('main.html', explanation=explanation, imgURL = imgURL, alt = description)

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
