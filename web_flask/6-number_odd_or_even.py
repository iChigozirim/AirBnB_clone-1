#!/usr/bin/python3
"""Starts Flask web application.
The application listens on 0.0.0.0, port 5000.
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display():
    """Displys 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_1():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_2(text):
    """Displays 'C' followed by the value of the text variable.
    Replaces underscore symbols with space in the variable.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/<text>", strict_slashes=False)
def display_3(text="is cool"):
    """Display “Python ”, followed by the value of the text
    variable (replace underscore _ symbols with a space ).
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def display_4(n):
    """Displays n if it is an integer."""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_5(n):
    """Displays a HTML page only if n is an integer."""
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def display_6(n):
    """Displays a HTML page only if n is an integer."""
    if n % 2 == 0:
        dtype = 'even'
    else:
        dtype = 'odd'
    return render_template('6-number_odd_or_even.html', number=n, dtype=dtype)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
