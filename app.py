from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/")
def fizzbuzz():
    return render_template('fizzbuzz.html')