from flask import Flask, render_template, request 
import sqlite3 
from flask import redirect

app = Flask(__name__)


@app.route("/")
def home():
    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    connection.close()
    return render_template("index.html", expenses=expenses)


@app.route("/about")
def about():
    return "<h1>About Expense Tracker</h1>"


@app.route("/contact")
def contact():
    return "<h1>Contact Page</h1>"

@app.route("/submit", methods=["POST"])
def submit():
    print("Submit function called")

    date = request.form["date"]
    category = request.form["category"]
    amount = float(request.form["amount"])
    description = request.form["description"]

    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        category TEXT,
        amount REAL,
        description TEXT
    )
    """)

    cursor.execute("""
    INSERT INTO expenses (date, category, amount, description)
    VALUES (?, ?, ?, ?)
    """, (date, category, amount, description))

    connection.commit()
    connection.close()

    print(date)
    print(category)
    print(amount)
    print(description)

    return redirect("/")

@app.route("/update/<int:id>", methods=["POST"])
def update(id):

    date = request.form["date"]
    category = request.form["category"]
    amount = float(request.form["amount"])
    description = request.form["description"]

    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE expenses
    SET
        date = ?,
        category = ?,
        amount = ?,
        description = ?
    WHERE id = ?;
    """, (date, category, amount, description, id))

    connection.commit()
    connection.close()

    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):

    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()      

    cursor.execute("""
    DELETE FROM expenses
    WHERE id = ?;
    """, (id,))

    connection.commit()
    connection.close()

    return redirect("/")
    
@app.route("/edit/<int:id>")
def edit(id):

    connection = sqlite3.connect("expenses.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT * FROM expenses
    WHERE id = ?;
    """, (id,))

    expense = cursor.fetchone()

    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    connection.close()

    return render_template(
        "index.html",
        expense=expense,
        expenses=expenses
    )


if __name__ == "__main__":
    app.run(debug=True)