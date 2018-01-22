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
@app.route('/process', methods=['POST'])
def submit():
    error = 0
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        error = 1
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        error = 1
    fname = str(request.form['fname'])
    lname = str(request.form['lname'])
    password = request.form['password']
    conf_password = request.form['conf_password']
    if len(fname) < 1:
        flash("First name cannot be blank!")
        error = 1
    if len(lname) < 1:
        flash("Last name cannot be blank")
        error = 1
    if len(password) < 1:
        flash("Password cannot be blank!")
        error = 1
    if len(conf_password) < 1:
        flash("Confirm Password cannot be blank!")
        error = 1
    if not str.isalpha(fname):
        flash("First names don't have numbers!")
        error = 1
    if not str.isalpha(lname):
        flash("Last names don't have numbers!")
        error = 1
    if len(password) < 8:
        flash("Your password must be at least 8 characters")
        error = 1
    if password != conf_password:
        flash("Your passwords do not match!")
        error = 1
    if error == 0:
        flash("Success!")
    return redirect('/')
app.run(debug=True)
