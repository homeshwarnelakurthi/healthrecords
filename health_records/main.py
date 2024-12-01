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

@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect("/")
    user_group = session.get("user_group")
    return render_template("dashboard.html", user_group=user_group)

@app.route("/view_records", methods=["GET", "POST"])
def view_records():
    if "username" not in session:
        return redirect("/")
    user_group = session.get("user_group")
    data = query_data(user_group)
    return render_template("view_records.html", records=data, user_group=user_group)



@app.route("/delete/<int:record_id>", methods=["POST"])
def delete(record_id):
    if "username" not in session or session.get("user_group") != "H":
        flash("You do not have permission to access this page.")
        return redirect("/dashboard")
    
    from access_control import delete_data
    success = delete_data(record_id)
    if success:
        flash(f"Record {record_id} deleted successfully.")
    else:
        flash(f"Failed to delete record {record_id}.")
    return redirect("/view_records")

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
