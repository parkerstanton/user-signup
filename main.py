from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('signup.html')

@app.route("/")

@app.route("/welcome")
def welcome_page():
    return render_template('welcome.html')
def 
app.run()
