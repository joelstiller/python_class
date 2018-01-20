from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/result', methods=['POST'])
def post_results():
   name = request.form['name']
   location = request.form['location']
   favorite = request.form['favorite']
   comment = request.form['comment']
   # redirects back to the '/' route
   return render_template("result.html", name = name, location = location, favorite = favorite, comment = comment)
app.run(debug=True) # run our server
