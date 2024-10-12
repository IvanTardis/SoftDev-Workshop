  # Ivan Gontchar
  # Belugas (Ivan, Colyi, Tanzeem)
  # SoftDev
  # K16: Take and Keep
  # 2024-10-09
  # time spent: tbd

from flask import Flask, render_template, request, session

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
    if 'username' in session:
        retu
    return render_template( 'login.html' ) # We predict this will work, and will simply render the template login.html

app.secret_key = "1234";

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
    #session['username'] = request.args['username']
    #print(request.cookies.get('username'))

    # return request.cookies.get('username')
    if request.method == 'GET':
        session['username'] = request.args['username']
        return "<h2>Ivan Gontchar<br>Belugas (Ivan, Colyi, Tanzeem)<br>SoftDev<br>K16: Take and Keep<br>2024-10-08<br>time spent: tbd</h2>HEYO!<br>You just submitted \"" + session['username'] + "\" via GET. Nice!<br><br>GET: this means your info is in the URL and is a passed to the console as a string with a size limit.<br>POST: this means your info is sent in the background with no size limit, so it's a little more secure."
    else:
        session['username'] = request.form['username']
        return "<h2>Ivan Gontchar<br>Belugas (Ivan, Colyi, Tanzeem)<br>SoftDev<br>K16: Take and Keep<br>2024-10-08<br>time spent: tbd</h2>HEYO!<br>You just submitted \"" + session['username'] + "\" via POST. Nice!<br><br>GET: this means your info is in the URL and is a passed to the console as a string with a size limit.<br>POST: this means your info is sent in the background with no size limit, so it's a little more secure."
    return "Your input: " + request.form['username'] + "<br>"  #response to a form submission



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
