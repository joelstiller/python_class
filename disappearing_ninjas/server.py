# import Flask
from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")
@app.route('/ninja/<arg>', methods=['GET'])
def ninja(arg):
    if arg not in ["blue", "red", "orange", "purple"]:
        arg = "error"
    return render_template('ninja.html', arg=arg)
@app.route('/ninja')
def noninja():
    return render_template('ninja.html', arg="everyone")
app.run(debug=True)