# Dualbeans (Ivan, Michelle)
# SoftDev
# K23: A RESTful Journey Skyward
# 2024-11-20
# time spent:

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
print(myLink)
myURL = urllib.request.urlopen(myLink)
print(myURL.geturl())
# print(myURL.info())

s = myURL.read()
# print(s)
dict = json.loads(s)
pprint.pp(dict)

imgURL = dict['url']
print(imgURL)