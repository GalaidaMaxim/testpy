from flask import Blueprint, request, render_template, redirect, session
from db import createUser, getUser

auth = Blueprint("auth", __name__)

@auth.route("/signup", methods = ['GET', "POST"])
def signup():
    if request.method == "POST":
        login = request.form['login']
        password = request.form['password']
        data = createUser(login, password)
        print(data)
        return redirect(f"/")
        
    else:
        return render_template("signup.html")

@auth.route("/signin", methods = ['GET', "POST"])
def signin():
    if request.method == "POST":
        login = request.form['login']
        password = request.form['password']
        data = getUser(login, password)
        print(data)
        session['user'] = data
        return redirect(f"/")
        
    else:
        return render_template("signin.html")

@auth.route("/logout")
def logout():
    session.pop("user")
    return redirect("/")