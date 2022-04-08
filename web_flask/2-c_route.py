#!/usr/bin/python3
"""Starts Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
        /: Displays 'Hello HBNB!'
        /hbnb: Displays 'HBNB'
        //c/<text>: Display “C ” followed by the value of
                    the text variable.
"""
from flask import Flask

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
    Replaces underscore symols with space in the variable.
    """
    for i in range(len(text) - 1):
        if text[i] == '_':
            text[i] = ' '
    return “C ” + "".join(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
