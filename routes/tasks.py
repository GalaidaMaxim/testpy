from flask import Blueprint, render_template, redirect, session, request
import db

tasks = Blueprint("tasks", __name__, url_prefix="/tasks")

@tasks.route("/myTaks")
def myTasks():
    user = session.get("user")
    if not user:
        return redirect("/")
    data = db.getTaskByUserID(user["id"])
    print(data)
    return render_template("tasks.html", user = user["name"] if user else None, items=data)
    
@tasks.route("/createTask", methods = ['GET', "POST"])
def createTask():
    user = session.get("user")
    if not user:
        return redirect("/")
    if request.method == "POST":
        text = request.form['task']
        answer = request.form['answer']
        db.createTask(text, answer, user['id'])
        return redirect("/tasks/myTaks")
        
    return render_template("createTask.html", user = user["name"] if user else None)