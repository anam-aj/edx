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
            return redirect("/")

        # Access month from form
        month = request.form.get("month")
        # Check validity of month
        if not month:
            return redirect("/")
        try:
            month = int(month)
        except ValueError:
            return redirect("/")
        if month < 1 or month > 12:
            return redirect("/")

        # Access day from form
        day = request.form.get("day")
        # Check validity of day
        if not day:
            return redirect("/")
        try:
            day = int(day)
        except ValueError:
            return redirect("/")
        if day < 1:
            return redirect("/")
        elif month == 2 and day > 29:
            return redirect("/")
        elif (month == 4 or month == 6 or month == 9 or month == 11) and (day > 30):
            return redirect("/")
        elif day > 31:
            return redirect("/")

        # Write data into database
        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)

        return redirect("/")

    else:
        # Get birthdays' data from database
        birthdays_info = db.execute("SELECT * FROM birthdays")

        # Renders birthdays page
        return render_template("index.html", birthdays=birthdays_info)
