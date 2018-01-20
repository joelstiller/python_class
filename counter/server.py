from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below
# our index route will handle rendering our form
@app.route('/')
def index():
  if 'counter' in session:
    session['counter'] = int(session['counter']) + 1
  else:
    session['counter'] = 1
  return render_template("index.html")
# this route will handle our form submission
@app.route('/ninja', methods=['POST'])
def ninja():
  session['counter'] = int(session['counter']) + 1
  return redirect('/')
@app.route('/hacker', methods=['POST'])
def hacker():
  session['counter'] = 0
  return redirect('/')
app.run(debug=True) # run our server