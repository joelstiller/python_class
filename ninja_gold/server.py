#Loading flask stuff
from flask import Flask, render_template, redirect, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'SuperSecret'

# Setting log file
log = 'May the odds be forever in your favor.\n'

#Root route
@app.route('/')
def index():
    if 'num' not in session:
        session['num']=0 
    if 'log' not in session:
        session['log']=[log] 
    return render_template('index.html', gold=session['num'])

#Game code
@app.route('/process_money/<loc>', methods=['POST'])
def process_money(loc):
    if loc == "Farm":
        gold = random.randrange(10, 21)
        msg = "Earned " + str(gold)+ " gold from the farm! " + str(datetime.now())+'\n'
        session['num']+=gold
        session['log'].append(msg)
    elif loc == "Cave":
        gold = random.randrange(5, 11)
        msg = "Earned " + str(gold)+ " gold from the cave! " + str(datetime.now())+'\n'
        session['num']+=gold
        session['log'].append(msg)
    elif loc == "House":
        gold = random.randrange(2, 6)
        msg = "Earned " + str(gold)+ " gold from the house! " + str(datetime.now())+'\n'
        session['num']+=gold
        session['log'].append(msg)
    else:
        coinflip = random.randrange(0,101)
        if coinflip > 50:
            gold = random.randrange(0, 51)
            msg = "You WON " + str(gold)+ " gold from the casino! " + str(datetime.now())+'\n'
            session['num']+=gold
            session['log'].append(msg)
        else: 
            gold = random.randrange(0, 51)
            msg = "You entered the casino and LOST " + str(gold) + " gold... Ouch " + str(datetime.now())+'\n'
            session['num']-=gold
            session['log'].append(msg)
    return  redirect('/')
app.run(debug=True)