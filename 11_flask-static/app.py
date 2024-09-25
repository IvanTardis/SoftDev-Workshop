# Ivan Gontchar
# Belugas(Tanzeem Hasan, Colyi Chen)
# SoftDev
# K11: Some Things Never Change
# 2024-09-26
# time spent: 1 hour

# DEMO
# basics of /static folder
import random
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

'''@app.route("/static/foo.html")
def h():
    print("the __name__ of this module is... ")
    print(__name__)
    return str(random.random())'''

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
