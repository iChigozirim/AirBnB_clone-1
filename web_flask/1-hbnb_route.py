#!/usr/bin/python3
"""Starts Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
        /: Displays 'Hello HBNB!'
        /hbnb: Displays 'HBNB'
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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
