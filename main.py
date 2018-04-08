from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    
    return render_template('signup.html')

@app.route("/", methods = ['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    vpassword = request.form['vpassword']
    email = request.form['email']

    username_error = ''
    password_error = ''
    vpassword_error = ''
    email_error = ''

    if (not username) or (username.strip() == ""):
        username_error = "Not a valid username"
        username = ''
        password = ''
        vpassword = ''
    else:
        if len(username) > 20 or len(username) < 3:
            username_error = "That username is too short/ long"
            username = ''
            password= ''
            vpassword = ''
    
    if (not password) or (password.strip() == ""):
        password_error = "Not a valid password"
        password = ''
    else:
        if len(password) > 20 or len(password) <3:
            password_error = "That password is too long/short"
            password = ''
    
    if (not vpassword) or (vpassword.strip() == ""):
        vpassword_error = "That's not a valid password"
        vpassword = ''
        password = ''
    if vpassword != password:
            vpassword_error = "Oops, your passwords don't match."
            vpassword = ''
            password = ''
    if email != "":
        if '@' not in email:
            email_error = "Oops, you're missing an '@' sign." 
            email = ''
            password = ''
            vpassword = ''
        elif '.' not in email:
            email_error = "Oops, you're missing a period!"
            email = ''
            password = ''
            vpassword = ''
        else:
            if len(email) > 20 or len(email) <3:
                email_error = "That email is too long/short"
                email = ''
    
    if not username_error and not password_error and not vpassword_error and not email_error:
        return render_template('welcome.html', username = username)
    else:   
        return render_template('signup.html', username_error = username_error, password_error = password_error, vpassword_error = vpassword_error, email_error = email_error, username = username, password = password, vpassword = vpassword, email = email)



app.run()
