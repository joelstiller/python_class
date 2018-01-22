from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/result', methods=['POST'])
def post_results():
   error = 0
   name = request.form['name']
   location = request.form['location']
   favorite = request.form['favorite']
   comment = request.form['comment']
   if len(name) < 1:
     flash('Name cannot be blank!')
     error = 1
   if len(comment) < 1:
     flash('You must enter a comment!')
     error = 1
   elif len(comment) > 120:
     flash('Comment must be less than 120 characters!')
     error = 1
   # redirects back to the '/' route
   if error == 1:
     return redirect('/')
   else:
    return render_template("result.html", name = name, location = location, favorite = favorite, comment = comment)
app.run(debug=True) # run our server
