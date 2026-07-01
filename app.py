from flask import Flask, render_template, request  

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return "<h1>About Expense Tracker</h1>"


@app.route("/contact")
def contact():
    return "<h1>Contact Page</h1>"

@app.route("/submit", methods=["POST"])
def submit():
    date = request.form["date"]
    category = request.form["category"]
    amount = float(request.form["amount"])
    description = request.form["description"]

    print(date)
    print(category)
    print(amount)
    print(description)

    return "Form Received!"


if __name__ == "__main__":
    app.run(debug=True)