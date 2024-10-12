  # Ivan Gontchar
  # Belugas (Ivan, Colyi, Tanzeem)
  # SoftDev
  # K16: Take and Keep
  # 2024-10-09
  # time spent: tbd

from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)    #create Flask object

app.secret_key = "1234";

@app.route(("/"), methods=['GET', 'POST'])
def home():
    if 'username' in session:
        return "Welcome back " + session['username']
    return "Hello Stranger."


@app.route(("/login") , methods=['GET', 'POST'])
def login():
    # right here we check if there was any submission with post
    if request.method == 'POST':
        # putting the username into our session
        session['username'] = request.form['username']

        # we tried this print below because we thought that request.cookies.get
        # was equivalent to request.form, based on the notes, however, this prints
        # "None". Perhaps the notes implied that by function it would be the same
        # but there are extra steps to set up the cookies
        #print(request.cookies.get('username'))

        #print(session['username'])

        # since user inputed something, send them to the home page
        return redirect(url_for('home'))
    # otherwise we display the login template
    return render_template( 'login.html' )

@app.route("/logout")
def logout():
    # when the user is logging out, take their info out of the session
    session.pop('username', None)
    # send them back to the login page
    return redirect(url_for('login'))



    # if request.method == 'GET':
    #     session['username'] = request.args['username']
    #     return "<h2>Ivan Gontchar<br>Belugas (Ivan, Colyi, Tanzeem)<br>SoftDev<br>K16: Take and Keep<br>2024-10-08<br>time spent: tbd</h2>HEYO!<br>You just submitted \"" + session['username'] + "\" via GET. Nice!<br><br>GET: this means your info is in the URL and is a passed to the console as a string with a size limit.<br>POST: this means your info is sent in the background with no size limit, so it's a little more secure."
    # else:
    #     session['username'] = request.form['username']
    #     return "<h2>Ivan Gontchar<br>Belugas (Ivan, Colyi, Tanzeem)<br>SoftDev<br>K16: Take and Keep<br>2024-10-08<br>time spent: tbd</h2>HEYO!<br>You just submitted \"" + session['username'] + "\" via POST. Nice!<br><br>GET: this means your info is in the URL and is a passed to the console as a string with a size limit.<br>POST: this means your info is sent in the background with no size limit, so it's a little more secure."
    # return "Your input: " + request.form['username'] + "<br>"  #response to a form submission



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
