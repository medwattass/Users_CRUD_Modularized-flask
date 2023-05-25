from flask import render_template, request, redirect
from CRUD_app import app
from CRUD_app.models.user import User

@app.route("/")
def home():
    users = User.get_all()
    print(users)
    return render_template("home.html", users = users)

@app.route("/add_new")
def add_new():
    return render_template("new.html")

@app.route("/edit/<int:user_id>")
def edit(user_id):
    user = User.get_one(user_id)
    return render_template("edit.html", user=user)

@app.route("/show/<int:user_id>")
def show(user_id):
    user = User.get_one(user_id)
    return render_template("show.html", user=user)

@app.route('/sucess', methods=["POST"])
def sucess():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.create_new(data)
    return redirect('/')

@app.route('/updated/<int:user_id>', methods=["POST"])
def updated(user_id):
    data = {
        "id": user_id,
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.update(data)
    return redirect('/')

@app.route('/delete/<int:user_id>', methods=["GET", "POST"])
def delete(user_id):
    User.delete(user_id)
    return redirect('/')