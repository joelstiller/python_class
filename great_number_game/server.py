from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below
# our index route will handle rendering our form
import random # import the random module
# The random module has many useful functions. This is one that gives a random number in a range

@app.route('/')
def index():
  if 'num' not in session:
    session['num'] = random.randrange(0, 101) # random number between 0-100
    session['correct'] = None
  return render_template("index.html")
# this route will handle our form submission
@app.route('/guess', methods=['POST'])
def guess():
  session['guess'] = request.form['guess']
  if int(session['num']) == int(session['guess']):
    session['correct'] = 'Yes'
  elif int(session['num']) > int(session['guess']):
    session['correct'] = 'Low'
  else:
    session['correct'] = 'High'
  return redirect('/')
@app.route('/replay', methods=['POST'])
def replay():
    session['num'] = random.randrange(0, 101) # random number between 0-100
    session['correct'] = None
    return redirect('/')
app.run(debug=True) # run our server