  # Ivan Gontchar
  # Belugas (Ivan, Colyi, Tanzeem)
  # SoftDev
  # K16: Take and Keep
  # 2024-10-09
  # time spent: tbd

from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


@app.route(("/"), methods=['GET', 'POST'])
def disp_loginpage():
    # print("\n\n\n")
    # print("***DIAG: this Flask obj ***")
    # print(app)
    # print("***DIAG: request obj ***")
    # print(request)
    # print("***DIAG: request.args ***")
    # print(request.args)
    # print("***DIAG: request.args['username']  ***")
    # print(request.args['username'])
    # print("***DIAG: request.headers ***")
    # print(request.headers)
    return render_template( 'login.html' ) # We predict this will work, and will simply render the template login.html


@app.route(("/auth") , methods=['GET', 'POST'])
def authenticate():
    # print("\n\n\n")
    # print("***DIAG: this Flask obj ***")
    # print(app)
    # print("***DIAG: request obj ***")
    # print(request)
    # print("***DIAG: request.args ***")
    # print(request.args)
    # print("***DIAG: request.args['username']  ***")
    # print(request.args['username'])
    # print("***DIAG: request.headers ***")
    # print(request.headers)
    #return "HEYO"
    if request.method == 'GET':
        return "<h2>Ivan Gontchar<br>Sky-High-Flyers (Ivan, Colyi, Jason)<br>SoftDev<br>K15 - Take & Give<br>2024-10-08<br>time spent: 1 hour</h2>HEYO!<br>You just submitted \"" + request.args['username'] + "\" via GET. Nice!<br><br>GET: this means your info is in the URL and is a passed to the console as a string with a size limit.<br>POST: this means your info is sent in the background with no size limit, so it's a little more secure."
    else:
        return "<h2>Ivan Gontchar<br>Sky-High-Flyers (Ivan, Colyi, Jason)<br>SoftDev<br>K15 - Take & Give<br>2024-10-08<br>time spent: 1 hour</h2>HEYO!<br>You just submitted \"" + request.form['username'] + "\" via POST. Nice!<br><br>GET: this means your info is in the URL and is a passed to the console as a string with a size limit.<br>POST: this means your info is sent in the background with no size limit, so it's a little more secure."
    #return "Your input: " + request.form['username'] + "<br>"  #response to a form submission



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
