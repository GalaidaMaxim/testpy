from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/<string:user>/")
def main_user(user):
    return render_template("main.html", user=user)

@app.route("/signup", methods = ['GET', "POST"])
def signup():
    if request.method == "POST":
        login = request.form['login']
        password = request.form['password']
        return app.redirect(f"/{login}")
        
    else:
        return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)

# pip install flask
# pip install flask_sqlalchemy
# swxfYxUYez8bvIWw