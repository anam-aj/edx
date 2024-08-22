import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # Access name from form
        name = request.form.get("name")

        # Check validity of name
        if not name:
            redirect("/")

        # Access month from form
        month = request.form.get("month")

        # Check validity of month
        if not month:
            redirect("/")
        try:
            month = int(month)
        except ValueError:
            redirect("/")
        if month < 1 or month > 12:
            redirect("/")

        # Access day from form
        day = request.form.get("day")

        # Check validity of day
        if not day:
            redirect("/")
        try:
            day = int(day)
        except ValueError:
            redirect("/")
        if day < 1:
            redirect("/")
        if month == 2 and day > 29:
            redirect("/")
        elif (month == 4 or month == 6 or month == 9 or month == 11) and (day > 30):
            redirect("/")
        elif day > 31:
            redirect("/")


        # Write data into database
        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)

        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html

        return render_template("index.html")
