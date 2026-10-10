from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/signup", methods = ['GET', "POST"])
def signup():
    if request.method == "POST":
        login = request.form['login']
        password = request.form['password']
        print(login, password)
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)

# pip install flask
# pip install flask_sqlalchemy