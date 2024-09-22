# your heading here

'''
DISCO:
<note any discoveries you made here... no matter how small!>
Some modules are not part of the standard library
pip = "pip installs python": command for downloading more packages from terminal
"$pip install flask": will fail at start or during install bc of machine
run "$python3 -m venv foo"
can do "l;" or maybe "ls-al" to see foo folder
cd into it and see that it has a virtual python environment
to activate go to home dir and "usrname@cslab3-24:~$ . path/to/foo/bin/activate"
success = (foo) before usrname
run "deactivate" when wanted
now you can use virtual machine wherever you are

QCC:
0. This syntax kind of reminded me of Java, especially when you open a file and you do something like "File x = new File(fileName.extension)"
1. The major point of reference for '/' is in terminal and it is used for direectory, particularly the root directory
2. This will print
3.
4.
5.
 ...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?