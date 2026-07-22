from flask import Flask, render_template, request, redirect
import database

app = Flask(__name__)


@app.route("/")
def home():
    # initialize the database if it hasn't been created yet
    database.init_db()
    expenses = database.get_all_expenses()
    total = database.get_total()
    return render_template("index.html", expenses=expenses, total=total)


if __name__ == "__main__":
    app.run(debug=True)