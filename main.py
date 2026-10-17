from flask import Flask, render_template, url_for, request
from db import createUser, getUserByID

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/<string:user>/")
def main_user(user):
    data = getUserByID(user)
    return render_template("main.html", user=data['name'])

@app.route("/signup", methods = ['GET', "POST"])
def signup():
    if request.method == "POST":
        login = request.form['login']
        password = request.form['password']
        data = createUser(login, password)
        print(data)
        return app.redirect(f"/{data['id']}")
        
    else:
        return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)

# pip install flask
# pip install flask_sqlalchemy
# swxfYxUYez8bvIWw