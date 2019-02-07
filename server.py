from flask import Flask, render_template
app= Flask(__name__)

@app.route('/')
def home():
    print("Hello World")
    return ("Hello World")

@app.route('/dojo')
def dojo():
    print("DOJO")
    return ("Dojo")

@app.route('/say/<username>')
def say(username):
    print("Hi Flask")
    print("Hi John")
    return "Hi %s" % username

@app.route('/repeat/<x>/<y>')
def rep35(x,y):
    return f"{y} "*int(x)

@app.route('/<x>')
def errormsg(x):
    print("Sorry! No response. Try again")
    return "Sorry! No response. Try again"

if __name__ == "__main__":
    app.run(debug=True)