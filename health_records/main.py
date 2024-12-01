from flask import Flask, render_template, request, redirect, session, flash
from db_setup import initialize_database
from authentication import authenticate_user
from access_control import query_data, update_data

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize the database when the app starts
initialize_database()

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        selected_group = request.form["user_group"]

        user_group = authenticate_user(username, password)

        if user_group:
            session["username"] = username
            session["user_group"] = selected_group  # Allow selection of group H or R
            flash(f"Logged in as {username} in group {selected_group}.")
            return redirect("/dashboard")
        else:
            flash("Invalid credentials. Please try again.")
            return redirect("/")
    return render_template("login.html")

