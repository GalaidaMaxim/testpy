from flask import Blueprint, render_template, redirect, session

tasks = Blueprint("tasks", __name__, url_prefix="/tasks")

@tasks.route("/myTaks")
def myTasks():
    user = session.get("user")
    if not user:
        return redirect("/")
    return render_template("tasks.html", user = user["name"] if user else None)
    
@tasks.route("/createTask")
def createTask():
    user = session.get("user")
    if not user:
        return redirect("/")
    
    return render_template("createTask.html", user = user["name"] if user else None)