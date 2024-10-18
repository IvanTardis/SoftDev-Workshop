  # Belugas (Ivan, Colyi, Tanzeem)
  # SoftDev
  # K18: Serving Looks
  # 2024-10-18
  # time spent: 5 mins

# DEMO
# basics of /static folder
import random
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
