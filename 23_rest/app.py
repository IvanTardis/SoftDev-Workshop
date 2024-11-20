# Dualbeans (Ivan, Michelle)
# SoftDev
# K23: A RESTful Journey Skyward
# 2024-11-20
# time spent:

from flask import Flask, render_template, request, session, redirect, url_for
import urllib.request

app = Flask(__name__)    #create Flask object

# makin' a supa-secret key
app.secret_key = "1234";
