from flask import Flask, render_template, url_for, request, session
from routes.auth import auth

app = Flask(__name__)
app.secret_key ="this_my_secret"
app.register_blueprint(auth)

@app.route("/")
def main():
    user = session.get("user")

    return render_template("main.html", user = user["name"] if user else False)




if __name__ == "__main__":
    app.run(debug=True)

# pip install flask
# pip install flask_sqlalchemy
# swxfYxUYez8bvIWw