from flask import Blueprint, session, redirect, render_template, request
import db
tasks = Blueprint("task", __name__, url_prefix="/tasks")

@tasks.route("/createTask", methods=["GET", "POST"])
def createTask():
    user = session.get("user")
    if request.method == "POST":
        task = request.form['task']
        answer = request.form['answer']
        result = db.createTask(task, answer, user['id'])
        if result:
            return redirect("/tasks/myTaks")
        else:
            return render_template("createTask.html", user=user["name"] if user else None)
    return render_template("createTask.html", user=user["name"] if user else None)

@tasks.route('/myTaks')
def myTasks():
    user = session.get("user")
    items = db.getTasksById(user['id'])
    return render_template("tasks.html", user=user["name"] if user else None, items=items)
    
