from flask import Blueprint, render_template, redirect, request, session
from db import createUser, getUser

auth = Blueprint("auth", __name__)

@auth.route("/signin", methods = ['GET', "POST"])
def signin():
    if request.method == "POST":
        login = request.form['login']
        password = request.form['password']
        if session.get("user"):
            return redirect("/")
        data = getUser(login, password)
        if data:
            session['user'] = data
            return redirect(f"/")
        else:
            return render_template("signin.html", errorMessage="Помилка входу")
        
    if session.get("user"):
        return redirect("/")
    
    return render_template("signin.html")


@auth.route("/signup", methods = ['GET', "POST"])
def signup():
    if request.method == "POST":
        login = request.form['login']
        password = request.form['password']
        
        data = createUser(login, password)
        if data:
            print(data)
            return redirect(f"/{data['id']}")
        else:
            return render_template("signup.html", errorMessage="Помилка реєстрації")        
  
    if session.get("user"):
        return redirect("/")
    
    return render_template("signup.html")


@auth.route("/logout")
def logout():
    user = session.get("user")
    if user:
        session.pop("user", None)
    return redirect("/")